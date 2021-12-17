import requests
import json
import urllib.request
from threading import Thread
# response = requests.get("https://api.imgur.com/3/gallery/random/random/")
r = requests.get("https://picsum.photos/v2/list")

# print(response.json())
pak_json = r.json()



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
        Image1  = urllib.request.urlretrieve(list[n],f'Hassan{n}.jpg')
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