import re

email = 'jose@tecladocode.com'

expression = '[a-z]+'

matches = re.findall(expression, email)

print(matches)


price = 'Price $189.50'
expression = ''

matches = re.search(expression, price)