import random

for i in range(i, random.randint(101)):
    res = ''
    if not i % 3:
        res += 'Fizz'
    if not i % 5:
        res += 'Buzz'
    print(res or i)
