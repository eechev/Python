
#this import will import the full module and this will required the use
#of the module.function syntax
import pizza

# to import just the the function you will use
# from pizza import make_pizza
# in this case no need to use the madule.function syntax
# also using the syntax
# from pizza import *
# will import all functions from the python module and 
# the mudule.function notation is not needed

def greet_user(name, age):

   print(f"Hi {name}")

   if age >= 65:
      print("You must be retired!")
   else:
      print("You are not retired yet.")


message = "Testing how to use input to retrieve user input!"
message += "\nPlease tell me your name:"

name = input(message)

age = int(input("Please tell me your age: "))

greet_user(name, age)

prompt = f"{name}, Tell me what size pizza you would like:"

pizzaSize = int(input(prompt))
pizzaToppings = []

print(f"Tell me what toppings you would like")

while True:
   top = input("topping('q' to end):")
   if top == 'q':
      break
   else:
      pizzaToppings.append(top)

pizza.make_pizza(pizzaSize, pizzaToppings)