# this is an example of a class generator
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0
        
    # this will allow us to call next(object)
    # note this does not use the yield keyword
    def __next__ (self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            # this will raise the StopIteration exception
            # which will tells python that we reached the end of the generator
            raise StopIteration
        

my_gen = FirstHundredGenerator()
print("Generator:")
print(my_gen.number)
print(next(my_gen))
print(next(my_gen))


# we can also construct an iterator
class FirstFiveIterator:
    def __init__(self):
        self.number = 0
        
    
    def __next__(self):
        if self.number < 5:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration

print("\nIterator:")        
my_iterator = FirstFiveIterator()
try:
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator)) # should throw StopIteration
except StopIteration:
    print("The iterator has reached the end")
    
    
# here I'm creating a class that will be an iterable
class FirstHundredIterable:    
    def __iter__(self):
        return FirstHundredGenerator()
    

#here I'm iterating over the iterable
for number in FirstHundredIterable():
    print(number)
    
    
#here I can't iterate over the generator
#for number in FirstHundredGenerator(): # this will throw an compile error because it is not iterable
#    print(number)


#can I make a generator iterable?
class FirstHundredGeneratorIterable:
    def __init__(self):
        self.number = 0
        
    def __iter__(self):
        return self
    
    def __next__ (self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            # this will raise the StopIteration exception
            # which will tells python that we reached the end of the generator
            raise StopIteration

print("\nGenerator as Iterable:")
# yes I can make a generator iterable as well
for number in FirstHundredGeneratorIterable():
    print(number)
    
    
# another example of an iterable
# where we define the __len__ and __getitem__ dunder methods
# making the class iterable
class AnotherIterable:
    def __init__(self):
        self.cars = ['Ford', 'Chevrolet', 'Toyota']
        
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]

myCars = AnotherIterable()

for car in myCars:
    print(car)
    
#this is a generator comprehension
print("\nGenerator Comprehension:")
myCars = (x for x in ['Ford', 'Chevrolet', 'Toyota', 'Honda'])
for car in myCars:
    print(car)
    
print(myCars)