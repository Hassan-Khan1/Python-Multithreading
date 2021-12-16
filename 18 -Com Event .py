from threading import Event,Thread
from time import sleep

# FLag is True with Set()  Method 
# Reset to False With  Clear() Method 
# Blocks until flag is True Wait()


def light_switch():
  sleep(3)
  e.set()
  print("Green Ligth ON")
  sleep(5)
  print("Red Light ON")
  e.clear()

def traffic():
  e.wait()
  while e.is_set():
    print("YOu Can GO")
    sleep(0.2)
    print("Program Done")

e = Event()

t1 = Thread(target=light_switch)
t2 = Thread(target=traffic)

t1.start()
t2.start()