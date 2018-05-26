'''
Chess king moves horizontally, vertically or diagonally to any adjacent cell.
Given two different cells of the chessboard, determine whether a king can go
from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
first two - for the first cell, and then the last two - for the second cell.
The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.
'''


'''
King piece in chess can move to any adjacent cell, that means given a coordinate of 2,2 the king can move to
1,2 3,2 for horizontal, 2,1 2,3 for vertical and then 3,3 1,3 1,1 3,1 for adjacent cells. 
Basically, it can move +1 in any direction. That is the pattern.
'''

c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())

if abs(c1 - c2) <= 1 and abs(r1 - r2) <= 1:
    print("YES")
else:
    print("NO")