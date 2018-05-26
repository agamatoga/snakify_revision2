li = [int(x) for x in input().split()]
max = max(li)
min = min(li)
idxOfMax = li.index(max)
idxOfMin = li.index(min)

'''
find max and min numbers in the list and then find the index of the two numbers of max and min. 
then swap the two elements and then print all the numbers in the resulting list 
'''

# swap functionality here with shortened syntax
li[idxOfMax], li[idxOfMin] = min, max

for eachNumber in li:
    print(eachNumber, end=" ")
