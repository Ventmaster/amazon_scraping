import multiprocessing
import subprocess

def run_app1():
    subprocess.run(["python", "app1.py"])

def run_app2():
    subprocess.run(["python", "app2.py"])

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_app1)
    p2 = multiprocessing.Process(target=run_app2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()