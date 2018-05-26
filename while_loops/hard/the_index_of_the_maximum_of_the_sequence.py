'''
A sequence consists of integer numbers and ends with the number 0.
Determine the index of the largest element of the sequence.
If the highest element is not unique, print the index of the first of them.
'''

max = 0
index_of_max = -1
ele = -1
len = 1

while ele != 0:
    # keep getting the element input as long as it is not 0
    ele = int(input())
    # the moment the element input is greater than current max set a new max to check against
    if ele > max:
        max = ele
        # the index_of_max will get set to len, we only set index for when it is greater
        index_of_max = len
    # increment the current index as it iterates through 
    len += 1

print(index_of_max)