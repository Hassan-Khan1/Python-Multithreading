
from threading import Thread

# with Argument
def thrd1(a):
  print("THread Runnig : ", a)


t = Thread(target=thrd1,args=(10,))

t.start()