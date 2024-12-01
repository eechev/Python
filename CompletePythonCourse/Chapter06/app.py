my_file_path = "D:/Projects/Python/CompletePythonCourse/Chapter06/data.txt"

my_file = open(my_file_path, 'r')
file_content = my_file.read()
my_file.close()
print(file_content)

user_name = input("What is your name? ")
my_file = open(my_file_path, 'w')
my_file.write(user_name)
my_file.close
