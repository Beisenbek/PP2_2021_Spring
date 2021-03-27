class Person:
  name = "John"
  age = 36
  country = "Norway"

p = Person()
p2 = Person()


p2.name = "Bob"
print(p2.name)
print(p.name)

print(getattr(p, 'page', 'my message'))
print(getattr(p2, 'page', 'my message2'))

print(getattr(p2, 'name', 'my message3'))







