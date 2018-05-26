'''
Medium

Given an integer. Print its tens digit.
'''

'''
Don't know why, but we don't have to know why.

Divide the number by 10, modulo by 10 to get tens digit!

This returns the tens digit.

The "%d" is a String format for digits, use it with % ( ... ) !

'''

n = int(input())

print("%d" % ((n/10) % 10))