from threading import Thread

# Thread Child Class with Constructor in Python


class MyThread1(Thread):
  def __init__(self,a):
    Thread.__init__(self)
    print("Child Thread Constructor : ",a)
  def run(self):
    pass

t = MyThread1(10 )
t.start()
print("Main Thread")