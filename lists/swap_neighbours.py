'''
Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.).
Print the resulting list. If a list has an odd number of elements, leave the last element in place.
'''

l = [int(x) for x in input().split()]


# run swaps
'''
start from index of 1 and go to the end of the list stepping by 2. Step by 2 means that the next number is always 
going to be odd. 

'''
for i in range(1, len(l), 2):
    l[i - 1], l[i] = l[i], l[i - 1] # swap the two in place

# join the result back into a String format
print(" ".join([str(i) for i in l]))