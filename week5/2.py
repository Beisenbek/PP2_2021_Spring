class Person:
  name = "John"
  age = 36
  country = "Norway"

p = Person()
p2 = Person()

p2.name = "Bob"


atrr = input()

print(getattr(p2, atrr, 'my message'))






