from __future__ import print_function

import os
import logging
import asyncio
import grpc
import proto.run_pb2 as run_pb2
import proto.run_pb2_grpc as run_pb2_grpc


def packProgram(program, tests, id):
    program = {
        "program": program,
        "tests": tests,
        "id": id
    }
    return program


def getPrograms():
    programsPath = os.path.join(os.path.abspath(os.curdir), "programs")
    programs = []
    for programName in os.listdir(programsPath):
        programPath = os.path.join(programsPath, programName, "prog.py")
        testsFolderPath = os.path.join(programsPath, programName, "tests")
        testsPath = [os.path.join(testsFolderPath, x) for x in os.listdir(testsFolderPath)]
        with open(programPath, "rb") as p:
            program = p.read()
        tests = []
        for testPath in testsPath:
            with open(testPath, "r") as t:
                test = t.read()
                tests.append(test)
        programs.append(packProgram(program, tests, programName))
    return programs


async def run() -> None:
    print("Try to connect to server...")
    async with grpc.aio.insecure_channel("localhost:5050") as channel:
        stub = run_pb2_grpc.RunnerStub(channel)
        programs = getPrograms()

        async def send_program(program):
            print(f"Send program {program['id']}")
            programPb = run_pb2.CodeWithTests(program_code=program["program"], tests=program["tests"], id=program["id"])
            response = await stub.CheckProgram(programPb)
            print(f"Get program {program['id']}")
            for i, res in enumerate(response.result):
                res = res[:-1]
                print(f"Test {i}:\n", res)

        tasks = [send_program(program) for program in programs]
        await asyncio.gather(*tasks)




if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
