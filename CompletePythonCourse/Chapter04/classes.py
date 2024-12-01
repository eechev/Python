my_student = {
    'name': 'Ralph Smith',
    'grades': [70, 88, 90, 99]
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))


class Student:
    # dunder init function also known in other languages as the constructor
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    
student_one = Student('Ralph Smith', [70, 88, 90, 99])

print(student_one.average())

student_two = Student("Joe Doe", (90, 99, 80))

print(student_two.average())