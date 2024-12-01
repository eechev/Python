#list comprehension
friends = ["Kevin", "Karen", "Jim", "Oscar", "Pam"]
friends_lower = [friend.lower() for friend in friends]
print(friends_lower)

numbers = [1, 2, 3, 4, 5]
doubled = [num * 2 for num in numbers]
print(doubled)

odds = [odd for odd in numbers if odd % 2 != 0]
print(odds)


guests = ["Kevin", "Karen", "Jim", "Oscar", "Jim", "Ralph", "Bob"]
friends_lower = {friend.lower() for friend in friends}
guest_lower = {guest.lower() for guest in guests}

present_friends ={friend.title() for friend in friends_lower.intersection(guest_lower)}

print(present_friends)

time_since_last_seen = [2, 3, 6, 5, 19]

long_timers = {
    friends[i] : time_since_last_seen[i]
    for i in range(len(friends))
    if time_since_last_seen[i] > 5
}

print(long_timers)

#using zip
friends = ["Kevin", "Karen", "Jim", "Oscar", "Pam"]
ages = [24, 25, 26, 27, 28]
friends_with_age = dict(zip(friends, ages))
print(friends_with_age)