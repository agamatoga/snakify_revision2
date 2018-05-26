'''

N students take K apples.

How many apples does each student get? How many remain in the basket?
'''

n = int(input())
k = int(input())

# Doing floor division will return the number of apples each student will get by taking off the decimal
print(k//n) # "Number of apples divided by number of students gives us number each student gets"

# Using modulo will give us the remaining apples in the basket
print(k % n) # Number of apples modulo number of students will give us the remainder 