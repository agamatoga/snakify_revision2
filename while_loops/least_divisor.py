'''
we want to find the divisor for a number n that is the smallest.
given that it will not be 2 and so the divisor can't be 1, so it must be at the least 2.
'''

n = int(input())

i = 2

'''
continuously check possible divisors and we know that it divides easily when the modulo of the number results 
in 0. Thus keep checking until that happens starting from possible least (2) and when thats done break out of the 
while loop and print the number. 
'''
while n % i != 0:
    i += 1
print(i)