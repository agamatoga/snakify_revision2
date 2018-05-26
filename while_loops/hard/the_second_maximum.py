'''
The sequence consists of distinct positive integer numbers and ends with the number 0.
Determine the value of the second largest element in this sequence.
It is guaranteed that the sequence has at least two elements.
'''


'''
what is the value of the second largest element in the sequence? 

first we need the maximum. Then we need to keep track of previous numbers 
'''

max = 0
prev_max = 0
n = int(input())

while n != 0:
    '''
    first we check the basic maximum and keep track of the second maximum in the case that n > max 
    '''
    if n > max:
        prev_max = max # keep record of prev_max which would be the second maximum
        max = n # set new max
    # however, if n < max but greater than prev_max set the prev_max to be n as that is the new second maximum
    elif n < max and n > prev_max:
        prev_max = n
    n= int(input())

print(prev_max)