from customthread import CustomThread
from threading import *
thread_dict = {}
started_list=[]

def create_thread(group=None, target=None, name=None,args=(),kwargs=None,daemon=None):
    """
    remeber that single-element tuple need the trailing comma to interpreted as a tuple
    """
    if name in thread_dict:
        raise Exception(f"thread with name {name} already exists")
    else:
        t1=CustomThread(group=group, target=target, name=name,daemon=daemon,args=args,kwargs=kwargs)
        thread_dict[name]=t1


def number_of_active_thread():
    print(active_count())
    

def check_alive(thread_name):
    return thread_dict[thread_name].is_alive()

def start_thread(name):
    if name not in thread_dict:
            raise Exception(f"thread with name {name} not registered")

    elif name in started_list:
        print("already started")
    else:    
            thread_dict[name].start()
            started_list.append(name)
         


def join_thread(name,timeout=None):
    """
    timeout just tell join how long to wait for the thraed to stop.if the thread is
    still running after the timeout expire the join calls ends,but thread keeps running.
    """
    print("function called")
    if name not in thread_dict:
            raise Exception(f"thread with name {name} not registered")

    elif name not in started_list:
        print("thread with name {name} not started".format(name=name))     

    else:
            thread_dict[name].join(timeout)
            if check_alive(name):
                pass
            else:
                return thread_dict[name].join()


def list_active_thread():
    """
    all thread who is currenty running
    """
    active_threads=enumerate
    for thread in active_threads:
        print("Thread Name",thread.name)  




#make sure before start
def set_thread_daemond(name):
    """
        whenever last Non-daemon thraed terminate automatically
        all daemon threads will be terminated
    """

    if name not in thread_dict:
            raise Exception(f"thread with name {name} not registered".format(name=name))

    else:
            thread_dict[name].setDaemon(True)


def terminate_all_threads():
    """ 
    after all the child thread complete and before main thread terminate i want same task then 
    i need call terminate_threads() after this i can that work
    """

    for thread_name in thread_dict:
        if check_alive(thread_name):
            thread_dict[thread_name].join()

def get_thread_id():
    return get_ident()

def get_status(name):
    if name not in thread_dict:
        print("thread with name {name} not initialiazed".format(name=name))
    elif name not in started_list:
        print("thread with name {name} not started".format(name=name))
    elif check_alive(name):
        print("thread with name {name} running".format(name=name))
    else:
        print("thread with name {name} finished".format(name=name))




















