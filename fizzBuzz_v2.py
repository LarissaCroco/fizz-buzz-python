def fizz_buzz(x):
    if x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    elif x % 3 == 0 and x % 5 == 0:
        return "Fizz Buzz"
    else:
        return x


for x in map(lambda number: fizz_buzz(number), range(1, 101)):
    print(x)

