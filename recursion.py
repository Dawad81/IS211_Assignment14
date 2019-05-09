#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring."""


def fibonacci(n):
    if n<0:
        print("Input must be a positive number!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print fibonacci(10)


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)



print gcd(30, 20)

# def compareTo(s1, s2):
#     if s1[0] < s2[0]:
#         return -1,compareTo(s1[1:], s2[1:])
#     elif s1[0] == s2[0]:
#         return 0,compareTo(s1[1:], s2[1:])
#     elif s1[0] > s2[0]:
#         return +1,compareTo(s1[1:], s2[1:])
#     #compareTo(s1[1:], s2[1:])
#
# print compareTo('Happy', 'Happer')


def compareTo(s1, s2):
    #s1= [i for i in s1]
    #s2= [i for i in s2]

    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return +1
    elif s1[0] == s2[0]:
        return 0, compareTo(s1[1:], s2[1:])




test = compareTo('cad', 'cad')
print test
