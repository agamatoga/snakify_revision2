li = [int(x) for x in input().split()]
ans = 0

for i in range(1, len(li) - 1):
    curr = li[i]
    nxt = li[i + 1]
    prev = li[i - 1]

    '''
    if the result is that the current one is both greater than the next and the previous, increase the count! 
    '''
    if curr > nxt and curr > prev:
        ans += 1

print(ans)
