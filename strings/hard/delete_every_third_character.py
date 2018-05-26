'''
Given a string. Delete from it all the characters whose indices are divisible by 3.
Remember that Strings are immutable in Pythhon
'''


s = input()
new_s = ""

for i in range(len(s)):
    if i % 3 != 0:
        new_s += s[i]

print(new_s)