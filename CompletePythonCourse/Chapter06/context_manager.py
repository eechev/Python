import json

json_file_path = "D:/Projects/Python/CompletePythonCourse/Chapter06/friends_json.txt"
car_json_file_path = "D:/Projects/Python/CompletePythonCourse/Chapter06/car_json.txt"

with open(json_file_path, "r") as file:
    file_content = json.load(file) #read files and turns it to a dictionary


for friend in file_content["friends"]:
    print(friend)
    
    
cars = [
    {'make': 'Ford','model': 'Mustang'},
    {'make': 'Chevrolet','model': 'Camaro'}
]

with open(car_json_file_path, "w") as car_json_file:
    json.dump(cars, car_json_file)
