from custom_function import *
from time import sleep
from datetime import datetime
def venue(venues):
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
    sleep(8)
    print('wedding date: 22/09/2021')        # join work as a await work in js 
    print("exception Handled")
    print('venue location printed:')
    return 20

def card_distribution():
    print('list of people')
    print('group people by region')
    sleep(10)
    print('select which person to go in which region')                          # first print card then we will distribute
    print('cards distributed')

venues=['noavailable','noavailable','noavailable','noavailable','noavailable','ttd']

create_thread(target=venue,name="venue_thread",args=(venues,))
create_thread(target=wedding_card,name="wedding_card_thread")
create_thread(target=card_distribution,name="card_distribution_thread")

start_thread("venue_thread")
start_thread("wedding_card_thread")
start_thread("card_distribution_thread")
join_thread("venue_thread")
now = datetime.now().time() # time object
print("now =", now)
join_thread("wedding_card_thread")
join_thread("card_distribution_thread")
number_of_active_thread()

now = datetime.now().time() # time object

print("now =", now)