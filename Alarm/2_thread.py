import threading
import time

def sleeper(s,name):
    print("Hi I'm {}. Going to sleep for 5 seconds\n".format(name))
    time.sleep(s)
    print("{} has woke up from sleep".format(name))

t=threading.Thread(target= sleeper, name="thread1", args=(5,'thread1'))

t.start()
t.join()

print("Hello")
print("Hello")


##### t.join() 없을 때
# Hi I'm thread1. Going to sleep for 5 seconds
# Hello
# Hello
# thread1 has woke up from sleep

##### t.join() 있을 때
#