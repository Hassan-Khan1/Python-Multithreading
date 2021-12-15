from threading import Thread


# Thread With Child Class And Main THread  Example
print("<----------------------------->")

def child():
  for i in range(3):
    print("Child Thread")

t = Thread(target=child)

t.start()

for i in range(3):
  print("Mian THread")