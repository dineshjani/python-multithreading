from threading import *
import time
lock=Lock()
def wish(name):

   with lock:  #lock will release automatically


        for i in range(10):

            print("Good Evening:",end='')
            time.sleep(2)
            print(name)
t1=Thread(target=wish,args=("Dhoni",))  #or we can pass lock as a argument
t2=Thread(target=wish,args=("Yuvraj",))
t3=Thread(target=wish,args=("Kohli",))
t1.start()
t2.start()
t3.start()

#difference between lock and rlock is that in rlock thread can acquire the same lock again and again.

# semaphore requirement when at a time particular number of thread are allowed to access. like 10 for db and 4 for network connection