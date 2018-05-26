'''
A sequence consists of integer numbers and ends with the number 0.
Determine how many elements of this sequence are equal to its largest element.
'''

'''
first find the maximum.
then keep count of how many in the sequence are equal to the maximum.
every time we find a new maximum the count needs to be reset. 
'''

n = int(input())
max = 0
count = 0

while n != 0:
    if n > max:
        max = n
        count = 0

    if n == max:
        count += 1

    n = int(input())

print(count)