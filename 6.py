from threading import Thread,currentThread


# We can also use name methode for setNAme and getName 

def disp():
  print("Default Child Thread Name : ",currentThread().name)
  currentThread().name = "Doc Thread"
  print("New Child Thread Name : ",currentThread().name)


t = Thread(target=disp)
t.start()

t.join()
print("Default Main THread  Name: ", currentThread().name)
currentThread().name = "Geeks Thread"
print("New Main THread  Name: ", currentThread().name)