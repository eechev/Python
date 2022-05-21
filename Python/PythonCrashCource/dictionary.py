# working with dictionaries, which in Python is a collection of key-value pairs.

#the creation of a dictionary
alien_0 = {'color':'green', 'points':5}
# how to access the value of each item in the dictionary
print(f"The alien color is {alien_0['color']} and he's worth {alien_0['points']} points")

#dictionaries are dynamic structures therefore they can be assigned addtional variables

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(f"All the attributes of alien 0: {alien_0}")

#creating an empty dictionary
alien_1 = {}

alien_1['color'] = 'brown'

print(f"New alien color is {alien_1['color']}")

#you can also delete an item from the dictionary

del alien_0['points']

print(f"All the attributes of alien 0: {alien_0}")

# using get() allowes you to query a key and not get an error when the key does not exist
# instead of an error you will get a nalue of None

print(f"The worth of alien 0 is {alien_0.get('points')}")
print(f"The worth of alien 1 is {alien_1.get('points')}")

#chapter 6 describes how to loop and how to create list of dictionaries

#one interesting thing is that a value can be a list for example

pizza = {
   'crust':'thick',
   'toppings': ['ham', 'pineapples']
   }

print(f"Nancy's favorite pizza is {pizza['crust']}-crust pizza "
      "with the following toppigs:")
for toppings in pizza['toppings']:
   print(f"\t{toppings}")