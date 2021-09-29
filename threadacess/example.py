from custom_function import *
from time import sleep
from datetime import datetime
def venue(venues):
    sleep(5)
    print(venues)
    raise Exception("hello")  #we can use here own custom exception
    for i in venues:                        
        if i != 'noavailable':
            print('venue fixed at :',i)
        else:
            print('venu not fixed:')
    return 10    

def wedding_card():
    print('bride name : anushka')
    print('groom name : virat')
    print('wedding date: 22/09/2021')        # join work as a await work in js 
    try:
        print(join_thread("venue_thread",3))                               # first decide venue then venue will print on card

    except Exception as e:
        print("exception Handled")
    print('venue location printed:')
    return 20

def card_distribution():
    print('list of people')
    print('group people by region')
    sleep(10)
    print('select which person to go in which region')
    print(join_thread("wedding_card_thread",3))                            # first print card then we will distribute
    print('cards distributed')

venues=['noavailable','noavailable','noavailable','noavailable','noavailable','ttd']

create_thread(target=venue,name="venue_thread",args=(venues,))
create_thread(target=wedding_card,name="wedding_card_thread")
create_thread(target=wedding_card,name="onlyregistered")


create_thread(target=card_distribution,name="card_distribution_thread")
start_thread("venue_thread")
start_thread("wedding_card_thread")
start_thread("card_distribution_thread")
get_thread_id()
number_of_active_thread()
""" 
after all the child thread complete and before main thread terminate i want same task then 
i need call terminate_threads() after this i can that work
"""

now = datetime.now().time() # time object

print("now =", now)
#wait for thread to finish
terminate_all_threads()   #all thread terminate except main 
print(get_thread_id())
now = datetime.now().time() # time object

print("now =", now)

print('Main Terminating')






"""
Daemonic threads can’t be joined. However, they are destroyed automatically when the main thread terminates.
"""
















