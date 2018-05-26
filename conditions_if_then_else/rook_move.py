'''
Chess rook moves horizontally or vertically.
Given two different cells of the chessboard, determine whether a
rook can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
first two - for the first cell, and then the last two - for the second cell.

The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.
'''


'''
A rook can only move if one of the two coordinates (X or Y) is the same as current. Otherwise, it cannot 
move to that cell. 

'''

c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

# c1 must be equal to c2 or r1 must be equal to r2 for the move to be possible
if c1 == c2 or r1 == r2:
    print("YES")
else:
    print("NO")