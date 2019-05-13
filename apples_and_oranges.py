#Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where is the start point, and is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .

#When a fruit falls from its tree, it lands units of distance from its tree of origin along the -axis. A negative value of means the fruit fell units to the tree's left, and a positive value of means it falls units to the tree's right.

#Given the value of for apples and oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.

st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

maca = 0

laranja = 0

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

for x in apples:
    if (x+a) >= s and (x+a) <= t:
        maca +=1
for x in oranges:
    if (x+b) >= s and (x+b) <= t:
        laranja +=1
    
print(maca)
print(laranja)
