from threading import Thread


import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s") % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
   # Thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   # Thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   t1 = Thread.start_new_thread(target=print_time, args=(2,))

except:
   print ("Error: unable to start thread")

while 1:
   pass