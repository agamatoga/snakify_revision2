'''
Given a string that may or may not contain the letter of interest. Print the index location of the second occurrence
of the letter f. If the string contains the letter f only once, then print -1, and if the string does not
contain the letter f, then print -2.
'''

'''
To tackle this problem we can find the index of the first occurrence and then the index of the last occurrence and then
find the second occurrence by finding the letter f within those two. 
'''

s = input()
f = "f" # letter to find
s_count = s.count(f) # gets the overall count
s1 = s.find(f) # finds the first occurrence of f
not_found = -2 # -2 for not found
found_one = -1 # -1 for found one

if s_count == 0:
    print(not_found)
elif s_count == 1:
    print(found_one)
else:
    '''
    otherwise find the first occurence of f within the index of the 
    from the first appearance onward 
    '''
    s2 = s.find(f,s1 + 1)
    print(s2)
