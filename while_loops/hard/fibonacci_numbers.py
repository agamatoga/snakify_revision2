'''
calculate the fibonacci sequence with a while loop.
remember that the fibonacci sequence is the sum of the previous two numbers
'''

n = int(input())

'''
we need two variables.
one to keep track of the previous sum.
another to keep track of the current sum which then becomes the previous sum. 
we then need to add the two numbers together, to get the current sum. 
'''

counter = 1
a = 0
b = 1
sum = 0

if n == 1:
    sum = 1
elif n == 0:
    sum = 0
else:
    while counter < n:
        sum = a + b

        a = b
        b = sum
        counter += 1

print(sum)

n = int(input())
if n == 0:
    print(0)
else:
# else a gets 0, b gets 1 as starting value
    a, b = 0, 1
# then for the range between 2 to n + 1 (because exclusive) you continue to add the sum
    for i in range(2, n + 1):
        # a will become b (previous sum) and b becomes (current sum which is previous sum in next iteration)
        a, b = b, a + b
    print(b)