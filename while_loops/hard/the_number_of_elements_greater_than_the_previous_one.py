
'''
given a sequence how many elements are greater than the previous number in the sequence?

'''


prev = int(input()) # current number
counter = 0
next = 0 # next number

while prev != 0:
    next = int(input()) # gets second input here
    if prev < next and next != 0: # second 0 check
        counter += 1
    prev = next # set prev current to current next

print(counter)
