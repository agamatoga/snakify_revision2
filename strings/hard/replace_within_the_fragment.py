'''
Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.
'''


'''
key here is "except for the first and last ones" meaning we can get the index of the first and the last and then
get the sequence of characters between the two. Once we get the sequence of characters between the two, run replace
and then concat again with the up-to-first occurrence and last occurrence and on Strings.
'''

s = input()

first = s.find('h') # gives us the first occurrence index
last = s.rfind('h') # gives us the last occurrence index

# get the inner sequence between the two of first and last
between = s[first + 1:last] # excluding last because we don't want to replace it, excluding the first as well
between_replaced = between.replace('h', 'H')

# re-concat and return the new String
print(s[:first + 1] + between_replaced + s[last:])