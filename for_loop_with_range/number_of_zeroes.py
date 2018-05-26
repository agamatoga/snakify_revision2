'''
Given N numbers: the first number in the input is N, after that N integers are given.
Count the number of zeros among the given integers and print it.
You need to count the number of numbers that are equal to zero, not the number of zero digits.
'''

# given N numbers, first number input is N
# after N int are given. Count number of
# zeros among the given integers and print
# count number of numbers equal to zero, NOT
# zero digits

n = int(input())
total = 0

for i in range(n):
    numToCheck = int(input())
    if numToCheck == 0:
        total += 1

print(total)
