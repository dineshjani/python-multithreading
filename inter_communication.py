from threading import *
import time
def producer():

    time.sleep(5)
    print("Producer thread producing items:")
    print("Producer thread giving notification by setting event")
    event.set()            #set a event

def consumer():
        print("Consumer thread is waiting for updation")
        event.wait()          #thread can wait untill event is set or not
        print("Consumer thread got notification and consuming items")

event=Event()
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()