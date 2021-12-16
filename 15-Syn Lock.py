from threading import *

class Filight:
  def __init__(self,available_seat):
    self.available_seat =available_seat
    self.l  = Lock()

  def reverse(self,need_seat):
    
    self.l.acquire()

    print("Available_Seat : ",self.available_seat)
    if(self.available_seat >= need_seat):
      name = current_thread().name
      print(f'{need_seat} seat is alloted for {name}')
      self.available_seat -= need_seat

    else:
      print("Sorry! All Seats HAs Alloted")

    self.l.release()

f = Filight(2)

t1 = Thread(target=f.reverse,args=(1,),name="Hassan")
t2 = Thread(target=f.reverse,args=(1,),name="ALi")
t3 = Thread(target=f.reverse,args=(1,),name="Dani")

t1.start()
t2.start()
t3.start()