import requests
import json
import urllib.request

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


list1 = ['https://picsum.photos/id/1023/3955/2094','https://picsum.photos/id/1024/1920/1280']
n = len(list1)
for i in range(n):

  urllib.request.urlretrieve(list1[i],f'Hassan{i}.jpg')

n = 0
try:
  # for n in  range(40):
  while True:
    pakg_str = json.dumps(pak_json[n]['download_url'])

    print(pakg_str.replace('"',''))
    n = n+1

    
    # urllib.request.urlretrieve(pakg_str,f'Hassan.jpg')

    # urllib.request.urlretrieve(pakg_str, "/home/hassan/Desktop/Python Threading/DDDDDD.jpg")
    # urllib.request.urlretrieve(pakg_str, filename)

except:
  
  print("Index is Out of Range")


