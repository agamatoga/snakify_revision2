'''
Given a string. Cut it into two "equal" parts (If the length of the string is odd, place the center character
in the first string, so that the first string contains one more characther than the second).
Now print a new string on a single row with the first and second halfs interchanged
(second half first and the first half second)
Don't use the statement if in this task.
'''

s = str(input())
# Two equal parts, if odd first half gets the extra character
# To make sure the first half gets the extra character if odd use modulo, and if its odd we can add the remainder
# to it

first_half = s[:(len(s) // 2) + (len(s) % 2)]
second_half = s[((len(s) // 2) + (len(s) % 2) + 1) - 1:]

# Print a new String with the halves interchanged
print(second_half + first_half)