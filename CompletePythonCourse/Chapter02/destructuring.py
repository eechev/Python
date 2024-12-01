currencies = (0.8, 1.2)
usd, eur = currencies #destructuring

print(usd)
print(eur)

friends = [("Kevin", 24), ("Karen", 25), ("Jim", 26)]

for name, age in friends:
    print(f"{name} is {age} years old.")
    
friend_ages = {"Kevin": 24, "Karen": 25, "Jim": 26}

#iterate through the dictionary and destructure the key and value
for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")