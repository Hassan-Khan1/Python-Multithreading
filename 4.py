from threading import Thread ,currentThread

# Set And Get THread 


# THread Methods
# Current Thread ,getNAme ,setName , name property_,


# Current Thread returns the  THread Name
# GetName Methode returns the Default Name of  THread Object


def disp():
  print("Child THread Name : ",currentThread().getName())

t1 = Thread(target=disp)
t2 = Thread(target=disp)

t1.start()
t2.start()

print("Main THread  : ", currentThread().getName())

