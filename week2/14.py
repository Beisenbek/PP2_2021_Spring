def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
x3 = myfunc(3)

print(mydoubler(11))
print(x3(11))