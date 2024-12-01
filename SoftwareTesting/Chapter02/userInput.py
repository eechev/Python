# taking user input
name = input("What is your name? ")
print(f"Hello, {name}")

# converting user input into a number 
size_input = input("How big is your house? (in square feet) ")
size = int(size_input)
square_meters = size / 10.8
print(f"Your house is {size} square feet or {square_meters:.2f} square meters")