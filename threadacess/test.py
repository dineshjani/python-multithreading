from custom_function import *
from time import sleep
from datetime import datetime

def wedding_card():
    print('bride name : anushka')
    sleep(10)
    

get_status("onlyregistered")   
create_thread(target=wedding_card,name="onlyregistered")
get_status("onlyregistered")   
now = datetime.now().time() # time object

print("now =", now)
print(start_thread("onlyregistered"))
now = datetime.now().time() # time object

print("now =", now)
get_status("onlyregistered")
join_thread("onlyregistered")
get_status("onlyregistered")   



