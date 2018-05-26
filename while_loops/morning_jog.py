# this is how many miles we can currently run
x = int(input())
# must be able to run y miles
y = int(input())

# increase = 10% from previous day, calculated every iteration
increase = x * .10
days = 1

while x < y:
    x += increase
    increase = x * .10
    days += 1

print(days)