# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

#hint: readlines()

people_file_path = "D:/Projects/Python/CompletePythonCourse/Chapter06/people.txt"
nearby_friends_file_path = "D:/Projects/Python/CompletePythonCourse/Chapter06/nearby_friends.txt"

friends = input("Enter 3 friend names separated by a comma(no spaces, please): ").split(",")
    
people_file = open(people_file_path, "r")
people = [line.strip() for line in people_file.readlines()]
people_file.close()

friends_set = set(friends)
people_set = set(people)

nearby_friends_set = friends_set.intersection(people_set)


nearby_friends_file = open(nearby_friends_file_path, 'w')
for friend in nearby_friends_set:
    print(f'{friend} is nearby')
    nearby_friends_file.write(f'{friend}\n')
    
nearby_friends_file.close()