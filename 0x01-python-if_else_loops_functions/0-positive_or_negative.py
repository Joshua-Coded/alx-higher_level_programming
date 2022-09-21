#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is Positive".format(number))
elif number == 0:
    print("{:d} is Zero ".format(number))
elif number < 0:
    print("{:d} is Negative".format(number))
