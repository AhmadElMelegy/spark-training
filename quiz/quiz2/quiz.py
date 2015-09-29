#!/usr/bin/env python

def my_print(x):
    if(x % 3 == 0 and x % 5 ==0):
        print "FizzBuzz"
    elif(x % 3 == 0):
        print "Fizz"
    elif(x % 5 == 0):
        print "Buzz"
    else:
        print x

map(my_print, range(1, 101))
