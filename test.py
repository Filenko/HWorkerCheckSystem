from multiprocessing import Pool, TimeoutError
import time
import os
import subprocess

def f(x):
    subprocess.run(["python3", "client.py"])

if __name__ == '__main__':
    with Pool(processes=30) as pool:
        print(pool.map(f, range(30)))