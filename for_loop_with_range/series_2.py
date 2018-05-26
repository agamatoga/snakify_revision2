'''
Given two integers A and B.
Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.
'''

# given a and b, print all numbers a to b
# inclusively in increasing order only if a < b
# if a >= b decreasing order
a = int(input())
b = int(input())

if a < b:
    for number in range(a,b + 1, 1):
        print(number)
else:
    for number in range(a,b - 1, -1):
        print(number)
