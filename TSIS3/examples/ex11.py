class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):     #__str__() function controls what should be returned when the class object is represented as a string
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()