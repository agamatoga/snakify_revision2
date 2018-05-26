'''
Medium

Given a three-digit number. Find the sum of its digits.
'''

n = str(input())
total = 0

for digit in n:
    total += int(digit)

print(total)


# Snakify version

n = int(input())
a = n // 100 # Gives ones place for three-digit number
b = n // 10 % 10 # Gives ten place
c = n % 10 # Gives one place
print(a + b + c)