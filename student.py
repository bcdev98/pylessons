class Person():
    def __init__(self, first_name, last_name, age):
        self.fname = first_name
        self.lname = last_name
        self.age = age
    
    def full_name(self):
        return self.fname + " " + self.lname


class Student(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
    
    def role(self):
        print("Student")
