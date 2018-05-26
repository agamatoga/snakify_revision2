'''
A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes.

A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
'''

a = int(input())
b = int(input())
n = int(input())

'''
100 cents in a dollar.
So cost is number of cupcakes multiplied by total cost in cents.

Once we have the total cost in cents, convert it back into dollar and cents by 
total cost in cents // 100 and the total cost % 100 to give you remainder after dollar (100 cents)
'''

cost = n * (100 * a + b)
print(cost // 100, cost % 100)