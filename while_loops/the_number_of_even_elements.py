
n = int(input())
evenCount = 0

while n != 0:
    if n % 2 == 0:
        evenCount += 1
    n = int(input())

print(evenCount)
