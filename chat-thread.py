from threading import Thread
from time import sleep

class MyThread1(Thread):
    def run(self):
        while True:
            msg=input('please give your name')
            print('u entered your name',msg)


class MyThread2(Thread):
    def run(self):
        while True:
            sleep(1)
           
            print("other  user said ......")   

t1=MyThread1()
t2=MyThread2()
t1.start()     #thread ko register ka kaam ye karega
t2.start()              