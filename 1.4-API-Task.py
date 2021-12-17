import requests
import json
import urllib.request
from threading import Thread,currentThread
import time
import random

r = requests.get("https://picsum.photos/v2/list")
pak_json = r.json()

class ImageDownload:
  def __init__(self):
      print("THread Name  Before: ",currentThread().getName())
      print("Image : Start")
      self.image()
      print("Image ENd")
      

  def image(self):
      # print("THread Name After: ",currentThread().getName())

      list = [] 
      random_num  = random.randint(0,25)
      pakg_str = json.dumps(pak_json[random_num]['download_url'])
      ss = pakg_str.replace('"','')
      list.insert(0,ss)
      ss = [random.choice('0123456789') for _ in range(1,5)]
      ss2 = "".join(ss)  
      # print(ss2 , time.thread_time())
      Image1  = urllib.request.urlretrieve(list[0],f'images/Imagee{ss2}.jpg')
      print(ss2, ' : ',list[0],' :  ',currentThread().getName())
      

class Multi_Thread:
  def thread_loop(self):
    for n in range(30):
      print("Thread Start::  " , n)
      # IM = ImageDownload()
      t = Thread(target=ImageDownload,name = f"THread Number : {n}")
      t.start()
      print("Thread End::  " , n)

   
T1 = Multi_Thread()
T1.thread_loop()

