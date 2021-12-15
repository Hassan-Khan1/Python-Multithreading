from threading import Thread
from typing_extensions import Self


# Thread Methods

# start()              
# run()       every thread  will run this  method when thread is started

# join wait till the thread  compleety executes()

print("<----------------------------->")
class MyThread(Thread):
  def run(self):
    print("RUn Method")
    for i in range(5):
      print("Child Thread")


t = MyThread()
print('Threading : ',t.name)
t.start()

for i in range(5):
      print("Child Thread")

t.join()

print("<----------------------------->")


# Thread Child Class with Constructor 

print("<----------------------------->")

class MyThread1(Thread):
  def __init__(self,a):
    Thread.__init__(self)
    print("Child Thread Constructor : ",a)
  def run(self):
    pass

t = MyThread1(10 )
t.start()
print("Main Thread")


print("<----------------------------->")


class Mythread11:
  def threadtt(self,a,b):
    print(a,b)

myt = Mythread11()

t = Thread(target=myt.threadtt,args= (10,20))
t.start()






print("<----------------------------->")
