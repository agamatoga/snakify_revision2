import math
'''
A car can cover distance of N kilometers per day.
How many days will it take to cover a route of length M kilometers?
The program gets two numbers: N and M.
'''

n = int(input())
m = int(input())

# We want worst case so do m / n and then run math.ceil to get the day rounded up!
print(math.ceil(m/n))