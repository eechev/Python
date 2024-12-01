#if statements

friends = ["Kevin", "Karen", "Jim"]
family = ["Pam", "Oscar", "Amy"]

# user_name = input("What is your name? ")

# if user_name in friends:
#     print("Hi friend!")
# elif user_name in family:
#     print("Hi family!")
# else:
#     print("Hi stranger!")
    
#while loops

# user_input = input("Do you wish to run the program? (y/n) ")

# while user_input == "y":
#     print("Running...")
#     user_input = input("Do you wish to run the program? (y/n) ")
    
# print("Goodbye")

# for loops is more like a for each loop

# for friend in friends:
#     print(friend)
    
# for i in range(1, 11):
#     print(i)

#break and continue

cars = ["ok", "ok", "ok", "ok", "ok", "ok", "faulty", "ok", "ok", "ok"]

print("Stopping at first fault")
for status in cars:
    if status == "faulty":
        print("Stopping the production line")
        break
    print(f"This car is {status}")

print("Skipping faulty cars")
for status in cars:
    if status == "faulty":
        print("Skipping faulty car")
        continue
    print(f"This car is {status}")
    
#else in for loops

for status in cars:
    if status == "faulty":
        print("Stopping the production line")
        break
    print(f"This car is {status}")
else:
    print("All cars built successfully")
    
good_cars = ["ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "ok"]

for status in good_cars:
    if status == "faulty":
        print("Stopping the production line")
        break
    print(f"This car is {status}")
else:
    print("All cars built successfully")
    
#else in while loops

print("Stopping at first fault")
i = 0
while i < len(cars):
    if cars[i] == "faulty":
        print("Stopping the production line")
        break
    print(f"This car is {cars[i]}")
    i += 1
else :
    print("All cars built successfully")
    
print("All good cars")
i = 0
while i < len(good_cars):
    if good_cars[i] == "faulty":
        print("Stopping the production line")
        break
    print(f"This car is {good_cars[i]}")
    i += 1
else :
    print("All cars built successfully")