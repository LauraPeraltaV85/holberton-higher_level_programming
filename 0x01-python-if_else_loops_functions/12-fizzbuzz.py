#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 is 0 and n % 5 is 0:
            print("FizzBuzz", end=' ')
        elif n % 3 is 0:
            print("Fizz", end=' ')
        elif n % 5 is 0:
            print("Buzz", end=' ')
        else:
            print("{}".format(n), end=' ')
