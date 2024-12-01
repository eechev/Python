# a prime number is a number that is only divisible by 1 and itself
for n in range(2, 24):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number")