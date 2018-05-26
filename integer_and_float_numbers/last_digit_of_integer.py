'''
Easy

Given an integer number, print its last digit.
'''

# We have two options here. Either turn the digit into a String and access it like a list
# Or use a built in functionality. Probably String will be more exam appropriate

n = int(input())

print(n % 10)

'''
So in Snakify what they do is do the number input % 10. 

This will return the last digit for every integer.

input % 10 returns the last digit for an integer!
'''
