from threading import Thread


# Creating a Thread without Creating Child Class to Thread Class in Python 


class Mythread11:
  def threadtt(self,a,b):
    print(a,b)

myt = Mythread11()

t = Thread(target=myt.threadtt,args= (10,20))
t.start()
 