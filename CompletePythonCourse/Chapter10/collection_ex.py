"""
* counter
* deque
* default dict
* ordered dict
* named tuple
"""

import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
    level=logging.DEBUG,
    filename='./Chapter10/app.log')

# counter
logging.info("This is a counter example")
print("Counter:")

from collections import Counter

device_temperature = [ 13.5, 14.0, 14.53, 15.0, 13.5, 13.5, 13.5]
# here we can count the number of times a value appears
temperature_counter = Counter(device_temperature)
print(temperature_counter[13.5])

# default dict
# it allows for us to create a dictionary with default values
print("Default Dict:")
from collections import defaultdict

coworkers = [
    ("Kevin", "MIT"),
    ("Karen", "Harvard"),
    ("Jim", "MIT"),
    ("Jim", "Harvard"),
    ("Oscar", "MIT"),
    ("Pam", "Harvard")
]

# here we iterate through the list of tuples and 
# check if the first element of the tuple is in the dictionary
# before add the default empty list
alma_maters_old = {}
for coworker, place in coworkers:
    if coworker not in alma_maters_old:
        alma_maters_old[coworker] = []
    alma_maters_old[coworker].append(place)
    
print(alma_maters_old)


# here we use the default dict to 
# create a dictionary with default values of empty lists
# eliminating two lines of code from above
alma_maters = defaultdict(list)
print(alma_maters)

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

print(alma_maters)

print(alma_maters["Kevin"])
print(alma_maters["Joan"]) # this will create a new key in the dictionary with default value

alma_maters.default_factory = None # this will make the default dict a normal dictionary
try:
    print(alma_maters["Joan"]) # this was already in the dictionary
    print(alma_maters["Peter"]) # this will throw a key error
except KeyError:
    print("The key is not in the dictionary")

# you can also use lambda functions when you want to use a variable
# to pass as a default value since defaultdict only allows functions as
# a parameter

my_company = "Chariot Pixels"

coworkers_company = defaultdict(lambda: my_company) # here we use a lambda function

print(f"Edgar works at {coworkers_company["Edgar"]}")


# Ordered Dict
print("Ordered Dict:")

from collections import OrderedDict

# here we create an ordered dictionary which is
# a dictionary that keeps the order of the items
# as they were added which a normal dictionary does since Python 3.7
o = OrderedDict()
o['Rolf'] = 6
o["Jen"] = 5
o["Charlie"] = 19

print(o)

#but ordered dict has a methods to move items and remove items
# here we move an item to the end
o.move_to_end("Rolf")
print(o)

# here we move an item to the beginning
o.move_to_end("Rolf", last=False)
print(o)

# here we remove an item by its key
o.pop("Rolf")
print(o)

# here we remove the last item
o.popitem()
print(o)


# Named Tuple
print("Named Tuple:")

from collections import namedtuple

# here we create a named tuple

Account = namedtuple('Account', ['name', 'balance'])

account = Account("checking", 1820.68,)
print(account.name)
print(account.balance)

myAccount = ('savings', 1000.00)

accountNamedTuple = Account(*myAccount)
print(accountNamedTuple.name)
print(accountNamedTuple.balance)


# Deque
print("Deque:")

from collections import deque

# here we create a deque which is a double ended queue
# which means we can add and remove items from both ends
d = deque((str(x) for x in ("Rolf", "Charlie", "Jose")))
d.append("Anna")
d.append("Manuel")
print(d)

d.appendleft("Oscar")
print(d)

d.popleft()
print(d)