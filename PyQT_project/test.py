import multiprocessing
import time

def fun1(argv1, argv2):
    while True:
        print("fun1", argv1, argv2)
        time.sleep(1)

def fun2():
    while True:
        print("fun2")
        time.sleep(1)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=fun1, args=("hello",))
    p2 = multiprocessing.Process(target=fun2, args=())
    p1.start()
    p2.start()