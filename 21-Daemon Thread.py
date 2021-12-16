

# Daemon Thread which runs in the BackGroud 
# Provides support to non-daemon Threads For his Success



# t1.setDaemon(True)         to make non-deamon thread to Deamon THread
# t1.daemon = True          to make non-deamon thread to Deamon THread


# Methods :

# setDeamon : is used  to set a thread to make him deamon thread

# Daemon Property: this property is used to check thread is deamon or not

# isDeamon() = is used to check whether a thread is deamon or not 

from threading import Thread, ThreadError, current_thread
from time import sleep

print("<------------------>")



# def disp():
#   print("Deamon Thread")

# t1 = Thread(target=disp)
# print('Before : ',t1.isDaemon())

# t1.setDaemon(True)

# print("After : ",t1.isDaemon())


# t1.start()


print("<------------------>")

# Default Nature of Thread

# Main THread is Always Non-Deamon THread

# Rest of the threads inherits deamon nature from their parents

  # if parent thread is non-deamon then child is also non-deamon
  # if parent thread is deamon then child is also deamon Thread

# When last Non-Daemon Thread terminates , automatically all deamon threads will be tenimated 



# if parent thread is non-deamon then child is also non-deamon
def disp():
  print("Disp Function")

mt = current_thread()
print(mt.getName())
print('MT : ',mt.isDaemon())
t1 = Thread(target=disp)
print('T1 : ',t1.isDaemon())
t1.start()



print("<------------------>")


# if parent thread is deamon then child is also deamon Thread

# def disp():
#   print("Disp Function")

#   t2= Thread(target=show)
#   print('T2 : ',t2.isDaemon())

#   t2.start()

# def show():
#   print("Show FUnction")
# mt = current_thread()
# print(mt.getName())
# print('MT : ',mt.isDaemon())

# t1 = Thread(target=disp)
# print('T1 Before : ',t1.isDaemon())
# t1.setDaemon(True)
# print('T1 After : ',t1.isDaemon())

# t1.start()
# t1.join()


print("<------------------>")


# When last Non-Daemon Thread terminates , automatically all deamon threads will be tenimated 


def teacher():
  for i in range(1,11):
    print("Teaching Session : ",i)
    sleep(1)

t1 = Thread(target=teacher)
t1.setDaemon(True)
t1.start()

sleep(6)
# t1.join()
print("Exam Finished",current_thread().name)


# Main kam jis pr things depend kare ge is Non-Deamon
# Suport mai chaiy os ko deamon banana h



print("<------------------>")
