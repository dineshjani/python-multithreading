from threading import *
import time
s=Semaphore(2)    #allow 2 thrread 
def wish(name):
        s.acquire()
        for i in range(10):
            print("Good Evening:",end='')
            time.sleep(1)
            print(name)
            print(active_count())
        s.release()

t1=Thread(target=wish,args=("Dhoni",))
t2=Thread(target=wish,args=("Yuvraj",))
t3=Thread(target=wish,args=("Kohli",))
t4=Thread(target=wish,args=("Rohit",))
t5=Thread(target=wish,args=("Pandya",))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


"""at a time lock object can be acquired by only one thread,but semaphore objects can be acuired 
by fixed numbers of thread specified by the counter value

main advantage of synchronization is we can overcome data inconsistencey problem.
but the main disadvantage of sync... is it increase waiting time of threads and create a performance problems.
hence there is no requirement then is not recommended to use synchronization(lock,semaphore,rlock)

"""

