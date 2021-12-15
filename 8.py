from threading import Thread

# Createing a thread by creating a child class to thread



class Mythread(Thread):
  def run(self):  
    for i in range(5):
      print("Child Thread")

t = Mythread()

t.start()

for i in range(5):
  print('Main Thread')