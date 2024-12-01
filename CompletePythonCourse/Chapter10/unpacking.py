#Unpacking

accounts = {
    'checking': 50.00,
    'savings': 100.00
}

def add_balance(amount: float, name: str = 'checking') -> float:
    """
    Function to update the balance and return the new balance
    """
    accounts[name] += amount
    return accounts[name]

print(add_balance(500.00))

print(add_balance(10.00, 'savings'))


# create a list of tuple transactions
transactions = [
    (100.00, 'checking'),
    (50.00, 'savings'),
    (103.00, 'checking'),
    (343.00, 'savings'),
    (-42.00, 'checking'),
    (12.00, 'savings'),
    (210.00, 'checking')
]

for t in transactions:
    add_balance(*t) #here we are unpacking the tuple
    

users = [
    {'username': 'rolf', 'password': '1234'},
    {"username": "jose", "password": "you_are_too"},
]

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        
user_objects = [User(**user) for user in users] # here we are unpacking the dictionary

for user in user_objects:
    print(user.username)
    print(user.password)