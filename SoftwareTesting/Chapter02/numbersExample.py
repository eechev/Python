from decimal import Decimal as D

f_price = 9.99
f_discount = 0.2
f_result = f_price * (1 - f_discount)
print(f_result)

price = D('9.99')
discount = D('0.2')
result = price * (1 - discount)
print(result)