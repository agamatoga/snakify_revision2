'''
Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
first two - for the first cell, and then the last two - for the second cell.
'''

'''
The pattern seems to be if you add up all the coordinates and modulo check for even, if its even
then its always the same color, otherwise its odd and not the same color!

'''

c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if (c1 + c2 + r1 + r2) % 2 == 0:
    print("YES")
else:
    print("NO")