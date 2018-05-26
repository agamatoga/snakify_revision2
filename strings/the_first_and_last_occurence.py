'''
find v. rfind

find will return the very first occurence of a substring
rfind will return the highest index occurence of the substring, i.e. the last
'''

s = input()
f = "f"
first = s.find(f) # find is the first occurence
last = s.rfind(f) # rfind is the last occurence

count_f = s.count(f) # gets the count of the substring f, i.e. how many occurences to know what to print

if count_f > 1:
    print(str(first) + " " + str(last)) # first occurence and last occurence
elif count_f == 1:
    print(first)
