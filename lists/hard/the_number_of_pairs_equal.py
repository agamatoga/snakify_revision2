'''
Given a list of numbers, count how many element pairs have the same value (are equal).
Any two elements that are equal to each other should be counted exactly once.
'''

'''
simply grab one element, iterate through the entire list again ( + 1 after element) and check for any matches, 
if there are any matches just +=1 the total count. 
'''

li = [int(x) for x in input().split()]
ele_pair_count = 0


for i in range(0,len(li)):
    # Take current i and check against all
    # then take next i and check against all
    # Iterate through list until each i has
    # been checked against all others
    holder = i
    for j in range(i + 1, len(li)):
        if li[holder] == li[j]:
            ele_pair_count += 1

print(ele_pair_count)
