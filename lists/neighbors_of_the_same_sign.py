l = [int(x) for x in input().split()] # convert the input into a list of int

'''
utilize the fact that to check if both are the same sign the multiplication of same signs is always positive 
'''
for i in range(0, len(l)):
    if l[i] * l[i + 1] > 0:
        print(l[i], l[i + 1])
        break
