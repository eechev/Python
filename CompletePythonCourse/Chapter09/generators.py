#this is a generator function, note the yield where the value is returned and the function stops or pauses
def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1
        
g = hundred_numbers()

print(next(g)) # this will print the first number and stop at the yield
print(next(g)) # this will print the next number and stop at the yield
print(next(g))

print(list(g)) # here it will print the rest of the list from where it left off from the last next command

my_range_obj = range(10)
print(my_range_obj) # this will print the repr of the range object

