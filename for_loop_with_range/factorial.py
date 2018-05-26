'''
Remember that Factorial 4! is 4 * 3 * 2 * 1
'''

n = int(input())
sum = 1

'''
Same result just thought about in an opposite manner, so instead of 4 * 3 * 2 * 1 it is 1 * 2 * 3 * 4 
'''
for i in range(1, n + 1):
    sum *= i

print(sum)
