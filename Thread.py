 
from threading import Thread ,current_thread


#  Creating a thread without using a class


# def disp():
#   print("Thread Running")
#   for i in range(5):
#     print("Child Thread")

# t = Thread(target=disp)
# t.start()
  
# for i in range(5):
#   print("Main Thread")




# def disp1(a,b):
#   print("Thread Running ---",a,b)
# t = Thread(target=disp1,args=(10,120))
# t.start()

# Set and Get Thread Name in Python


def disp22():
  print("Child Thread Object : " ,current_thread().getName())

t = Thread(target = disp22)
t.start()

print("Main Thread : ",current_thread().getName())
