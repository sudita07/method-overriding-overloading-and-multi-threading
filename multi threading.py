from threading import*
import time


class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            time.sleep(1)
class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            time.sleep(1)
t1=hello()
t2=hi()
t1.start()
time.sleep(0.2)
t2.start()