from threading import Thread
from queue import Queue
from time import sleep

# Queue Methods

# Put Method is used to insert items  into queue
# get method is used by consumer to retrieve items fromt the queue
# empty method return True if queue is Empty else returns False
# Full method return True if queue if Full else returns False


class Produce:
  def __init__(self):
    self.q = Queue()

  def produce(self):
    for i in range(1,6):
      print("Item Produce : ",i)

      self.q.put(i)
      sleep(1)

class Consumer:
  def __init__(self,prod):
    self.prod = prod

  def consume(self):
    for i in range(1,6):
      print("Item Received : ", self.prod.q.get(i))

p = Produce()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()