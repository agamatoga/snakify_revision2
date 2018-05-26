'''
k is the number of equal portions we want.
n * m is the total portions.

First we check that the number of portions we want is less than total available portions.

"Determine whether it is possible to split it so that one of the parts will have exactly k squares."

Then we need to determine if split is possible so one part will have exactly k squares, i.e. n or m part. 
'''

n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')