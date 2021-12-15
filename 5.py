from threading import Thread,currentThread


# Set-NAme is used to set the name of the naem of the thread 

def disp():
  print("Default Child Thread Name : ",currentThread().getName())
  currentThread().setName("Doc Thread")
  print("New Child Thread Name : ",currentThread().getName())


t = Thread(target=disp)
t.start()

t.join()
print("Default Main THread  Name: ", currentThread().getName())
currentThread().setName("Geeks Thread")
print("New Main THread Name : ", currentThread().getName())


print("<------------------------------->")


print("<------------------------------->")
