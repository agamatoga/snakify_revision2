sum = 0
flag = True

while flag:
    curr = int(input())
    if curr != 0:
        sum += curr
    else:
        flag = False


print(sum)
