from threading import Thread
from time import sleep
# Single Tasking using a Thread in Python 



class MyExm:
  def solve_question(self):
    self.q1()
    self.q2()
    self.q3()

  def q1(self):
    print("Question 1 Sovled")
    sleep(3)
  def q2(self):
    print("Question 2 Sovled")
    sleep(3)
  def q3(self):
    print("Question 3 Sovled")
    sleep(3)
mye = MyExm()

t = Thread(target=mye.solve_question)
t.start()

