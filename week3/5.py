class Person:
  def __init__(self, fname, lname):
    print("parent's consructor")  
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    print("child's consructor")  
    Person.__init__(self, fname, lname)
    

x = Student("John", "Doe")
x.printname()

