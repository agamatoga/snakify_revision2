'''
get the index of a fibonacci number

'''

# so while we calculate fibonacci numbers, grab the index of each one and the moment we hit the fibonacci number
# that it wants break out and return the index

z = int(input())

if z == 0:
    print(0)
else:
    a, b = 0, 1
    n = 1
    while b <= z:
        if b == z:
            print(n)
            break
        a, b = b, a + b
        n += 1
    else:
       print(-1)
        