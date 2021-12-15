from threading import Thread,currentThread


# We can also use name methode for setNAme and getName 

# we can also set and get thread name outside the function
print("<------------------------------->")

def disp():
    pass

t = Thread(target=disp)

# print(t.getName())
# t.setName("New Thread")
# print(t.getName())
print("<------------------------------->")

# using name
print("<------------------------------->")

s = Thread(target=disp)

print("Default",t.name)
t.name = "New Thread"
print("NEw",t.name)

print("<------------------------------->")

# Also we can set when we craete object 

# t = Thread(target=disp ,name= "Hassan THread")
# print(t.name)
print("<------------------------------->")
