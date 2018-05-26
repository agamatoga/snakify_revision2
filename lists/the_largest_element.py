'''
simply use the built in Python function of max() to find the max integer in the list
and then use the built in index() to find the index of that
'''

li = [int(x) for x in input().split()]

max = max(li)
idx = li.index(max)

print(max, idx)