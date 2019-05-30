#!/usr/bin/python3
'''
Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
'''
import numpy as np
n,m,p=map(int,input().split())
A = np.array([input().split() for i in range(n)], int)
B = np.array([input().split() for i in range(m)], int)
print(np.concatenate((A,B), axis=0))
