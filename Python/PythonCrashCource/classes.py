#creating classes in Python
# is there a way to make member variables private???

class Dog:
   """A simple class to model a dog"""

   #constructor
   def __init__(self, name, age):
      """Initialize member variables"""
      self.name = name
      self.age = age

   def sit(self):
      """Simulate a dog sitting in response to the command sit"""
      print(f"{self.name} is now sitting.")

   def roll_over(self):
      """Simulate a dog rolling over in response to the command to roll over"""
      print(f"{self.name} rolled over!")

#class inheritance, note the call to the super class init
class GermanSheppard(Dog):

   def __init__(self, name, age):
      super().__init__(name, age)
      self.weight = 15
      self.type = 'German Sheppard'

   def weight(self):
      print(f"{self.weight} lbs")


my_dog = Dog('Willie', 3)
my_germanSheppard = GermanSheppard('Bruce', 1)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

print(f"My other dog name is {my_germanSheppard.name}, and he's a {my_germanSheppard.type}.")


my_dog.sit()
my_dog.roll_over()