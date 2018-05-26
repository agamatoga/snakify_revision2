'''
Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, use the
method count ...
'''


'''
the count method returns the number of occurences of a certain substring. Meaning that to count the words what we can 
do is just count the number of whitespaces and then add 1, which will convert to the number of words in the String! 
'''

s = str(input())

print(s.count(" ") + 1)