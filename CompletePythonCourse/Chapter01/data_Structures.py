#List
print("List")
friends = ["Kevin", "Karen", "Jim"] #python does not enforce homegenous lists is up to you
print(friends)
print(len(friends))
print(friends[0])
print(friends[1])
print(friends[2])

friends_with_age = [
    ["Kevin", 24], 
    ["Karen", 25], 
    ["Jim", 26]
]

print(friends_with_age)
print(friends_with_age[0])
print(friends_with_age[1])
print(friends_with_age[2])

print(f"{friends_with_age[0][0]} is {friends_with_age[0][1]} years old.")
print(f"{friends_with_age[1][0]} is {friends_with_age[1][1]} years old.")
print(f"{friends_with_age[2][0]} is {friends_with_age[2][1]} years old.")

friends.append("Oscar")
print(friends[3])


friends.remove("Jim")
print(friends)

#tuples are immutable, therefore cannot be appended but you can add tuples together
print("Tuple")
short_tuple = "Kevin", "Karen", "Jim"
a_better_way = ("Kevin", "Karen", "Jim")
tuple_in_list = [("Kevin", 24), ("Karen", 25), ("Jim", 26)]

appended_tuple = short_tuple + a_better_way
print(appended_tuple)

#sets are unique, don't keep order or keep duplicates
print("Sets")
set_of_friends = {"Kevin", "Karen", "Jim", "Jim"}
print(set_of_friends)
set_of_friends.add("Oscar")
set_of_friends.add("Oscar")
print(set_of_friends)
set_of_friends.remove("Jim")
print(set_of_friends)

#advanced sets
art_friends = {"Jim", "Karen", "Oscar"}
science_friends = {"Derek", "Charlie", "Karen"}
friends_in_common = art_friends.intersection(science_friends)
print(friends_in_common)
friends_in_art_but_not_science = art_friends.difference(science_friends)
print(friends_in_art_but_not_science)
friends_in_science_but_not_art = science_friends.difference(art_friends)
print(friends_in_science_but_not_art)
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

#dictionaries are key value pairs, are mutable are ordered and cannot have duplicates keys
print("Dictionaries")
dict_of_friend_ages = {"Kevin": 24, "Karen": 25, "Jim": 26}
print(dict_of_friend_ages)
print(dict_of_friend_ages["Kevin"])

dict_of_friend_ages["Oscar"] = 25
print(dict_of_friend_ages)

#tuples with dictionaries
friends = (
    {"name": "Kevin", "age": 24},
    {"name": "Karen", "age": 25},
    {"name": "Jim", "age": 26},
)

print(friends[0]["name"] + " is " + str(friends[0]["age"]) + " years old.")

#lists with dictionaries
friends = [
    {"name": "Kevin", "age": 24},
    {"name": "Karen", "age": 25},
    {"name": "Jim", "age": 26},
]

print(friends[0]["name"] + " is " + str(friends[0]["age"]) + " years old.")

#converting a list of tuples to a dictionary
print("Converting a list of tuples to a dictionary")
friends_list_tuple = [
    ("Kevin", 24),
    ("Karen", 25),
    ("Jim", 26),]
print(friends_list_tuple)
friends_with_age = dict(friends_list_tuple)
print(friends_with_age)

#joining to print a list
friends = ["Kevin", "Karen", "Jim"]
print(", ".join(friends))

tuple_of_friends = ("Kevin", "Karen", "Jim")
print(", ".join(tuple_of_friends))

dict_of_friends = {"Kevin": 24, "Karen": 25, "Jim": 26}
print(", ".join(dict_of_friends)) #this will print the keys of the dictionary, not the values (dict_of_friends)
print(", ".join(str(x) for x in dict_of_friends.values())) #this will print the values of the dictionary