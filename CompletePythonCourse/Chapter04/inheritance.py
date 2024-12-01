class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
        
    def average_grade(self):
        return sum(self.marks) / len(self.marks)
    
    def add_mark(self, mark):
        self.marks.append(mark)
    

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


ralph = WorkingStudent("Ralph", "MIT", 16.00)
print(ralph.salary)
ralph.add_mark(90)
ralph.add_mark(100)
print(ralph.average_grade())