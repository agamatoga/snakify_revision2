'''
Given a list of numbers with all of its elements sorted in ascending order,
determine and print the quantity of distinct elements in it.
'''

l = [int(x) for x in input().split()]

'''
as long as the next one is different to the one prior to it, then that number is distinct and increase the count.
otherwise, its not and keep count the same.
'''

count = 1

for i in range(0, len(l) - 1):
    if l[i] != l[i + 1]:
        count +=1

print(count)