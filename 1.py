# Creating a Thread without using a Class 

from threading import Thread

print("<----------------------------->")


def thrd():
  print("THread Runnig")


t = Thread(target=thrd)

t.start()

print("<----------------------------->")


# with Argument
def thrd1(a):
  print("THread Runnig : ", a)


t = Thread(target=thrd1,args=(10,))

t.start()


print("<----------------------------->")

# Thread With Child Class And Main THread  Example

def child():
  for i in range(5):
    print("Child Thread")

t = Thread(target=child)

t.start()

for i in range(5):
  print("Mian THread")


print("<----------------------------->")
