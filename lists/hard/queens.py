'''
In chess it is known that it is possible to place 8 queens on an 8×8 chess board such that none of them can attack
another. Given a placement of 8 queens on the board, determine if there is a pair of queens that can attach each other
on the next move. Print the word NO if no queen can attack another, otherwise print YES.
The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a
standard chess board with rows and columns numbered starting at 1.
'''

'''

'''

# board of 8x8
n = 8
# first create the board
x = []
y = []

for i in range(0, n):
    '''
    you get 8 different inputs, for each input you split it into its x and y coordinates you split each one up
    into its own list and then append appropriately
    '''
    new_x, new_y = [int(i) for i in input().split()]
    x.append(new_x)
    y.append(new_y)

cannot_attack = True

'''
if a queen can attack another queen that means that it is in its line of fire, i.e. directly horizontal,
diagonol, vertical to it. 

thus we need to check if the x values are the same, y values are the same, or if the diagonol is the same which is 
done by the difference between the two x and y. 

To check for the adjacent possibility with the diagonol what we need to do is find the difference between
x and y and check if those differences are the same. If they are, they can attack eachother. 

So below we are doing all three checks and then iterating for all 8 checking whether 
the x value of the first, can attack the x value of the second.
the y value of the first, can attack the y value of the second.
and then the diagonol differences of the first and second differences. 
'''
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            cannot_attack = False

if cannot_attack:
    print("NO")
else:
    print("YES")