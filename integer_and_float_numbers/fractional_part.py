'''
Given a positive real number, print its fractional part.
'''


n = float(input())

'''
By doing subtraction between float and int() - which cuts off the fractional bit it'll give you the fractional
part as the result!

'''
print(n - int(n))