n = int(input())
i = 1

'''
continue to square the value and check if it is less than or equal to n. 
every time we increment i by 1 to get the next possible squared value 
'''
while i ** 2 <= n:
    print(i ** 2)
    i += 1