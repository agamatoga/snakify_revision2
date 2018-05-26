'''
Given three integers, determine how many of them are equal to each other.
The program must print one of these numbers: 3 (if all are the same), 2
(if two of them are equal to each other and the third is different) or 0 (if all numbers are different).
'''

a = int(input())
b = int(input())
c = int(input())

if a == b and b == c and c == a:
    print(3)
elif a == b or a == c or c == b:
    print(2)
else:
    print(0)