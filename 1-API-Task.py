import requests
import json
import urllib.request
from threading import Thread
import time
import random

# response = requests.get("https://api.imgur.com/3/gallery/random/random/")
r = requests.get("https://picsum.photos/v2/list")

# print(response.json())
pak_json = r.json()

# pakg_str = json.dumps(pak_json,indent=2).count
# print(pakg_str)
# https://picsum.photos/id/0/5616/3744

# urllib.request.urlretrieve('https://picsum.photos/id/0/5616/3744','Hassan.jpg')
    # urllib.request.urlretrieve(pakg_str, "/home/hassan/Desktop/Python Threading/DDDDDD.jpg")
    # urllib.request.urlretrieve(pakg_str, filename)

# list1 = ['https://picsum.photos/id/1023/3955/2094','https://picsum.photos/id/1024/1920/1280']
# n = len(list1)
# for i in range(n):
#   urllib.request.urlretrieve(list1[i],f'Hassan{i}.jpg')

# n = 0
# list = [] 
# try:
#   # for n in  range(40):
#   while True:
#     pakg_str = json.dumps(pak_json[n]['download_url'])
#     ss = pakg_str.replace('"','')

#     list.append(ss)
#     # Image  = urllib.request.urlretrieve(list[n],f'Hassan{n}.jpg')
#     # print(list[n])
    
#     n = n+1

# except:
#   print(n)
#   print("Index is Out of Range")


class ImageDownload:
  
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
        print(ss2 , time.thread_time())
        Image1  = urllib.request.urlretrieve(list[n],f'Image{ss2}.jpg')
        

        print(list[n],' :  ',n ,)
        n = n+1
    except:
      print(n)
      print("Index is Out of Range")


p = ImageDownload()

t1 = Thread(target=p.image)
t2 = Thread(target=p.image)

t1.start()
t2.start()

t1.join()
t2.join()

print("Main Thread")