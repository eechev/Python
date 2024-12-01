#lambda function are used to get input and give an output

divide = lambda x, y: x / y

print(divide(10, 2))

#you can use lambda functions to do a quick math without having to create a function

print((lambda x, y: x / y)(10, 2))