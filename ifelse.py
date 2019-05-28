#!/usr/bin/python3
'''
Given an integer, N, perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of 2 to 5, print Not Weird
If N is even and in the inclusive range of 6 to 20, print Weird
If N is even and greater than 20, print Not Weird
'''
N = int(input('give me a number '))

if N % 2 == 0:
    if N in range (2, 5):
        print('Not Weird')
    if N in range (6, 21):
        print('Weird')
    if N >= 22:
        print('Not Weird')
else:
    print('Weird')   
