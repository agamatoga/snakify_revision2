'''
There was a set of cards with numbers from 1 to N. One of the card is now lost.
Determine the number on that lost card given the numbers for the remaining cards.
Given a number N, followed by N − 1 integers - representing the numbers on the remaining
cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.
'''

n = int(input())
sum_cards = 0

# First sum up all the cards that should be the resulting sum
for i in range(1, n + 1):
    sum_cards += i


# Then begin to subtract the sum and the resulting sum is the missing card because you subtract
# every possible card number and whats remaining is the zero sum meaning no cards are missing
# or the card number which is missing because that is what is remaining in the sum subtraction
for i in range(n - 1):
    sum_cards -= int(input())

print(sum_cards)


'''
5 is the missing card.

1 + 2 + 3 + 4 + 5 = 15 

Subtract 
15 - 1 - 2 - 3 - 4 = 5 
'''