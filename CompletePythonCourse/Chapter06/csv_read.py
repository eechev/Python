file_to_read = "D:/Projects/Python/CompletePythonCourse/Chapter06/csv_data.txt"

file = open(file_to_read, 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]] #remove whitespace from each line and header

for line in lines:
    person_data = line.split(",")
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()
    
    print(f'{name} is {age}, studying {degree} at {university}.')