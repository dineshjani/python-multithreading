from threading import *
import time
def wish(name):

    for i in range(10):
        print("Good Evening:",end='')
        time.sleep(2)
        print(name)
        
t1=Thread(target=wish,args=("Dhoni",))
t2=Thread(target=wish,args=("Yuvraj",))
t1.start()
t2.start()