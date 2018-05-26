'''
Given a string consisting of exactly two words separated by a space.
Print a new string with the first and second word positions swapped (the second word is printed first).
'''

s = input()
s = s.split(" ")
s1 = s[0]
s2 = s[1]

new_s = s2 + " " + s1
print(new_s)
