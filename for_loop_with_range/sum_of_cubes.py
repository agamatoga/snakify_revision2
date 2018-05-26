# for given integer N, calculate sum:
# cube each number until N !

n = int(input())
sum = 0

for i in range(n + 1): # n + 1, because we want the numbers up to the actual (inclusive) number!
    iCubed = i ** 3
    sum += iCubed

print(sum)