'''
Given a list of numbers, find and print the elements that appear in the list only once.
The elements must be printed in the order in which they occur in the original list.
'''

'''
you can take each element in the list, hold the value and check it against all other values.
if the value appears again break and start the outer loop again for the next value, otherwise, if you iterate
through the entire list and not find an appearance, print it out.

remember that break breaks out of the current loop not exit the entire program. 
'''

l = [int(x) for x in input().split()]
count = 0

for i in range(len(l)):
    hold = l[i]
    count += 1
    for j in range(len(l)):
        if hold == l[j] and i != j:
            break
    else:
        print(l[i], end=" ")
