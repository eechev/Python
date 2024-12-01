class Foo:
    @classmethod #decorator where you want to use a class method
    def hi(cls):
        print(cls.__name__)
        
    @staticmethod #decorator and used best when you have a class that won't be inherited
    def bye():
        print("Bye")


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
        
    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"
    
    @classmethod #example of a class method
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"
        
    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        
    @property
    def average_grade(self):
        if self.marks == []:
            return 0
        
        return sum(self.marks) / len(self.marks)
    
    def add_mark(self, mark):
        self.marks.append(int(mark))
    

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
        
    @property # decorator property for methods that does not take any arguments and returns a value like a getter method
    def weekly_salary(self):
        return self.salary * 40
  
#example of a property  
john = WorkingStudent("John", "MIT", 16.00)
john.add_mark(90)
john.add_mark("100")
print(john.weekly_salary)
print(john.average_grade)

#example of a class method and static method
my_object = Foo()
my_object.hi()
my_object.bye()


#example of a class method
number = FixedFloat(3.14342342)
print(number)
print(number.from_sum(1, 2))

money = Euro(10)
print(money)
print(money.from_sum(10, 20))
#or you can do this
print(Euro.from_sum(50, 30))