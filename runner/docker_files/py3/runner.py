import subprocess
import resource
import click

def setlimits_linux():
    # Set limit for CPU time to 1 second
    resource.setrlimit(resource.RLIMIT_CPU, (1, 1))
    # Set limit for max number of subprocesses to 0
    # resource.setrlimit(resource.RLIMIT_NPROC, (0, 0))
    # Set limit for stack size to 32Mb
    # resource.setrlimit(resource.RLIMIT_STACK, (16 * 1024 * 1024, 32 * 1024 * 1024))

def RunProgram(progPath, testPath):
    with open(testPath, encoding="utf-8") as f_in:
        try:
            result = subprocess.Popen(
                ["python3", progPath],
                stdout=subprocess.PIPE,
                stdin=f_in,
                encoding="utf-8",
                preexec_fn=setlimits_linux,
                restore_signals=True
            )
        except subprocess.TimeoutExpired:
            print("Time Limit Exceeded")
        except Exception as e:
            print("1231313", e)

        print(result)
        rr = result.stdout.read()
        print(rr)


        with open("result", "w") as r:
            r.write(rr)

        return rr


@click.command()
@click.option('--prog-path', help = "Path to program to execute")
@click.option('--test-path', help='Path to test for program')
def main (prog_path, test_path):
    a = RunProgram(progPath=prog_path, testPath=test_path)
    return a

if __name__ == "__main__":
    main()

