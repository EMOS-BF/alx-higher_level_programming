#!/usr/bin/python3
number = 0
while number <= 99:
    if number != 99:
        print("{:02d} ".format(number), end='')
    else:
        print("{:02d}\n".format(number))
    number = number + 1
