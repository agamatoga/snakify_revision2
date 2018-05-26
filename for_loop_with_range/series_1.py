'''
Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.
'''


# Important to note: Python range is exclusive, meaning it starts from inclusive but the end is exclusive!
a = int(input())
b = int(input())

for x in range(a,b + 1):
    print(x)