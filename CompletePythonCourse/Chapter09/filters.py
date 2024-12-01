print("Filters example:") 
# the filter function must return True or False
def starts_with_k(friend):
    return friend.startswith("K")

friends = ["Kevin", "Karen", "Jim", "Oscar", "Pam"]

# you define the filter function and then call it
# also this filter function returns an iterator and 
# you need to convert it to a list or you can use a next
start_with_k = filter(starts_with_k, friends)

# once this is done you can't iterate over the filter start_with_k
friend_list = list(start_with_k)
print("Iterating through the iterator:")

try:
# the stop iteration exception will be raised
    print(next(start_with_k))
except StopIteration:
    print("The iterator has reached the end")

#but when saved as a list you can iterate over it
print("\nList:")
for friend in friend_list:
    print(friend)

print("\nList:")
for friend in friend_list:
    print(friend)

# you can also use a lambda function
print("\nLambda:")
start_with_k_2 = filter(lambda friend: friend.startswith("K"), friends)
print(list(start_with_k_2))

# another way is to use a generator comprehension
print("\nGenerator Comprehension:")
start_with_k_3 = (friend for friend in friends if friend.startswith("K"))
print(list(start_with_k_3))