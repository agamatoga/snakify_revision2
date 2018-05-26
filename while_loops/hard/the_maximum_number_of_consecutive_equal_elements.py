'''
Given a sequence of integer numbers ending with the number 0.
Determine the length of the widest fragment where all the elements are equal to each other.
i.e. keep track of repeats
'''



'''
initialize with:
prev variable which tracks the previous number of input to compare the next to 
current repetition length 
maximum repetition length
'''
prev = - 1
curr_rep_len = 0
max_rep_len = 0

ele = int(input())

while ele != 0:
    '''
    if we find a match, increase the current repetition length by 1 
    '''
    if prev == ele:
        curr_rep_len += 1
    else:
        '''
        otherwise, we set a new prev, and look for the next match and then choose the new maximum based on old 
        length and currently maximum and then reset the current length 
        '''
        prev = ele
        max_rep_len = max(curr_rep_len, max_rep_len)
        curr_rep_len = 1 # reset curr length
    ele = int(input())

# finally get the maximum by doing it one more time in the case prev was == to ele and we have a new curr length
# to make sure our max is the correct maximum
max_rep_len = max(curr_rep_len, max_rep_len)

print(max_rep_len)
