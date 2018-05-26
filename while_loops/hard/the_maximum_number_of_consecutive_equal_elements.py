'''
Given a sequence of integer numbers ending with the number 0.
Determine the length of the widest fragment where all the elements are equal to each other.
'''

'''
keep track of one number, the moment we find another number that is equal to the currently held we need 
to find the number of steps we just went till we found that equal number.

once we have the steps for one, we need to start over and keep track of the distance between the next two.
if the distance between the next two we get is greater, then that means we've got to replace the current maximum steps 

'''