'''
In Python we can reverse a String by using the ::-1 extended slice syntax!

'''

s = input()
h = "h"
h_first = s.find(h) # first occurence
h_last = s.rfind(h) # second occurence
seq_enc = s[h_first:h_last + 1] # the enclosed sequence of strings
seq_rev = seq_enc[::-1] # reverse the enclosed sequence of strings

'''
the answer is then the three concatenated above 
'''

ans = s[:h_first] + seq_rev + s[h_last + 1:]
print(ans,end='')

