

s = input()
h = "h"
first_h = s.find(h) # find first occurrence of  h
second_h = s.rfind(h) # find last occurrence of h

'''
get the new string by slicing up to the first index (exclusive!)
and then get the second half by slicing from the second occurrence of h 
and onward (+1 because beginning index is inclusive) 
'''
new_s = s[:first_h] + s[second_h + 1:]

print(new_s)
