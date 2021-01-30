x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print(x)

myfunc()

print("Python is " + x)