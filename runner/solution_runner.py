from .loader import Loader
from .executor import Executor
from .solution import Solution

class SolutionRunner():
    def __init__(self):
        self.results = []
        self.loader = Loader()
        self.executor = Executor()
    def RunProgram(self, program, test):
        self.loader.ClearRunningDirectory()
        self.loader.LoadProgram(program)
        self.loader.LoadTest(test)
        return self.executor.Py3Execute()

    def RunSolution(self, solution: Solution):
        for test in solution.tests:
            self.results.append(self.RunProgram(solution.programCode, test))