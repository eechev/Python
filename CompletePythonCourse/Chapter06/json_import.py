import json

json_file_path = "D:/Projects/Python/CompletePythonCourse/Chapter06/friends_json.txt"
car_json_file_path = "D:/Projects/Python/CompletePythonCourse/Chapter06/car_json.txt"

json_file = open(json_file_path, "r")
file_content = json.load(json_file) #read files and turns it to a dictionary
json_file.close()

for friend in file_content["friends"]:
    print(friend)
    
    
cars = [
    {'make': 'Ford','model': 'Mustang'},
    {'make': 'Chevrolet','model': 'Camaro'}
]

print(cars)

car_json_file = open(car_json_file_path, "w")
json.dump(cars, car_json_file)
car_json_file.close()