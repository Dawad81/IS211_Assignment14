#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module creates recursive functions."""


def fibonacci(n):
    if n<0:
        print("Input must be a positive number!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)



def compareTo(s1, s2):
    #Hi Professor,
    # i could not figure out how to get my results with out it returning tuples
    #in time. i hope i came close.
    # if possable, can you send me the correct code to make this function work?
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return +1
    else:
        if len(s1) == len(s2):
            for item in s1:
                if s1[0] < s2[0]:
                    return -1
                elif s1[0] > s2[0]:
                    return +1
                elif s1[0] == s2[0]:
                    return 0, compareTo(s1[1:], s2[1:])



