import requests
import json
import urllib.request
from threading import Thread
import time
import random

r = requests.get("https://picsum.photos/v2/list")
pak_json = r.json()

class ImageDownload:
  def __init__(self,num_of_threads):
      self.num_of_threads =num_of_threads
      print(self.num_of_threads)
      threads = []
      print("00000")
      for n in range(self.num_of_threads):
          t = Thread(target=self.image())
          print("333333")
          t.start()
          threads.append(t)

  # def TT(self):
      

  def image(self):
    n = 0
    list = [] 
    try:
      # for n in  range(40):
      while True:
        pakg_str = json.dumps(pak_json[n]['download_url'])
        ss = pakg_str.replace('"','')
        list.append(ss)

        ss = [random.choice('0123456789') for _ in range(1,5)]
        ss2 = "".join(ss)  
        # print(ss2 , time.thread_time())
        Image1  = urllib.request.urlretrieve(list[n],f'images/Image{ss2}.jpg')
        

        print(ss2, ' : ',list[n],' :  ',n ,)
        n = n+1
    except:
      print(n)
      print("Index is Out of Range")

# class DT:
#   def __init__(self,num_of_threads):
#       self.num_of_threads =num_of_threads
#       print(self.num_of_threads)
#       print("0000011")

#   def TT(self):
#       threads = []
#       print("0000011")

#       for n in range(self.num_of_threads):
#           t = Thread(target=self.image())
#           print("333333")
#           t.start()
#           threads.append(t)


# TT = DT(10)
# TT.TT()
IM = ImageDownload(10)

IM.TT()

# t1 = Thread(target=p.image)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Main Thread")

# p = ImageDownload
# o = 10
# # t1 = Thread(target=p.image)
# for h in range(o):
#   t1 = Thread(target=p.image)
#   t1.start()