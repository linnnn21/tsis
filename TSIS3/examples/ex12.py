class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def full_name(self):
        return f"{self.firstname} {self.lastname}"


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # Родительский конструктор
        self.graduationyear = year      # Новый атрибут

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

s1 = Student("Tim", "Akin", 2025)
s1.welcome()  
