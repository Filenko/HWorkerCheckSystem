import grpc
import runner.proto.run_pb2 as run_pb2
import runner.proto.run_pb2_grpc as run_pb2_grpc
import asyncio
import logging
from .solution import Solution
from .solution_runner import SolutionRunner

logger = logging.getLogger("my_logger")
logging.basicConfig(level=logging.DEBUG, format="%(message)s")



class Runner(run_pb2_grpc.RunnerServicer):
    async def CheckProgram(
            self,
            request: run_pb2.CodeWithTests,
            context: grpc.aio.ServicerContext,
    ) -> run_pb2.CheckResults:
        solution = Solution(request.program_code.decode(), request.tests, request.id)
        runner = SolutionRunner()
        runner.RunSolution(solution=solution)
        print(runner.results)
        return run_pb2.CheckResults(id = solution.id, result = runner.results)

async def serve() -> None:
    server = grpc.aio.server()
    run_pb2_grpc.add_RunnerServicer_to_server(Runner(), server)
    listen_addr = "[::]:5050"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


