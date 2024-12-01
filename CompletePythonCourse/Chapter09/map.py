# a map function is a function that takes in a function and a iterable and returns a iterable of the 
# results of applying that function to each element of the iterable

friends = ["Kevin", "Karen", "Jim", "Oscar", "Pam"]

friends_lower = map(lambda friend: friend.lower(), friends)

# other ways to do the same thing as above
friends_lower_list_comprehension = [friend.lower() for friend in friends]
friends_lower_generator_expression = (friend.lower() for friend in friends)

print(list(friends_lower))
print(friends_lower_list_comprehension)
print(list(friends_lower_generator_expression))


# another example of using a map function

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data["password"])
    
users_list = [
    {"username": "rolf", "password": "1234"},
    {"username": "jose", "password": "youaretoo"},
]

users = map(User.from_dict, users_list)

print(users)

for user in users:
    print(user)
    print(user.username)
    print(user.password)