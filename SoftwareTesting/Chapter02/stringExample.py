name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

## templates

greeting_template = "Hello, {}"

with_name = greeting_template.format(name)

print(with_name)

name = "Ralph"
with_name = greeting_template.format(name)  
print(with_name)

longer_phrase = "Hello, {}! How are you today? Today is {}."

with_name_and_date = longer_phrase.format(name, "Monday")
print(with_name_and_date)