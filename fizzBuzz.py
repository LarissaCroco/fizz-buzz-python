def print_fizz(number):
    print("Fizz")


def print_buzz(number):
    print("Buzz")


def print_fizz_buzz(number):
    print("Fizz Buzz")


for x in range(1, 101):
    if x % 3 == 0:
        print_fizz(x)
    elif x % 5 == 0:
        print_buzz(x)
    elif x % 3 == 0 and x % 5 == 0:
        print_fizz_buzz(x)
    else:
        print(x)
