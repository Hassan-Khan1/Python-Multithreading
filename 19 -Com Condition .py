from threading import Thread , Condition
from time import sleep


# Methods
# notify is to wake up  thread on the condition default (n = 1)
#   notify(n = 1)


lst  = []

def produce():
  cv.acquire()
  for i in range(1,6):
    lst.append (i)
    sleep(1)
    print("Item Produced....")

  cv.notify()
  cv.release()

def consume():
  cv.acquire()
  cv.wait(timeout=0)
  cv.release()
  print(lst)
  
cv = Condition()

t1 = Thread(target=produce)
t2 = Thread(target=consume)

t1.start()
t2.start()