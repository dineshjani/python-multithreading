from threadacess.customthread import CustomThread as Thread
list_thread=[]                                  #we make here class and make a custom class 
                            #where class have own action instance and exception method
                            #we have to implement dict with  {threadname,thraedobject}                     
def register_thread(action,*arguments):
    print(len(list_thread))
    if arguments==None:                   #check already registered or not
        t1=Thread(target=action)
    else:
        t1=Thread(target=action,args=(arguments))
 

    list_thread.append(t1)

def stop_thread(action):
    for thread in list_thread:
        if thread.target==action:
            list_thread.remove(thread)
            thread.stop()

def start_thread(action):
    for thread in list_thread:
        if thread.target==action:
            thread.start()

def join_thread(action):
    for thread in list_thread:
        if thread.target==action:
            thread.join()


"""register_thread(venue,venues)
register_thread(wedding_card)
register_thread(card_distribution)

start_thread(venue)
start_thread(wedding_card)
start_thread(card_distribution)"""