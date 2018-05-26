'''
even elements printed in the list but not over indices, do it for each item individually
so if each item in the list is even print it, otherwise don't
'''

li = input().split()

for item in li:
    if int(item) % 2 == 0:
        print(item)
