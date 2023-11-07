import os
import shutil
import subprocess

class Loader():
    def __init__(self):
        self.path = "/home/run"

    def DumpStringToFile(self, inputString, name):
        savePath = os.path.join(self.path, name)
        with open(savePath, "w") as f:
            f.write(inputString)

    def LoadProgram(self, program, path = "/home/run"):
        self.DumpStringToFile(program, "prog.py")
        subprocess.run(["chown", "-R", "run:run", "/home/run"], user="root")

    def LoadTest(self, test, path = "/home/run"):
        self.DumpStringToFile(test, "test.in")
        subprocess.run(["chown", "-R", "run:run", "/home/run"], user="root")

    def ClearRunningDirectory(self, path = "/home/run"):
        for root, dirs, files in os.walk('/home/run'):
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))
        # shutil.rmtree('/tmp/')
        # shutil.rmtree('/var/tmp')