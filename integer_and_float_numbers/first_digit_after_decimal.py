'''
Given a positive real number, print its first digit to the right of the decimal point.

'''

n = float(input())

'''

By taking the float and multiplying it by 10 and modulo by 10 you get the first digit to the right after 
decimal point!
'''
print(int(n * 10) % 10)