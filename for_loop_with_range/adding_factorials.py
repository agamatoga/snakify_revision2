'''
Given an integer n, print the sum 1!+2!+3!+...+n!.
This problem has a solution with only one loop, so try to discover it. And don't use the math library :)
'''

# Print the sum of all factorials

n = int(input())
sum = 1
sum2 = 0

for i in range(1,n + 1):
    sum *= i 
    sum2 += sum # adds sums of factorials

print(sum2)
