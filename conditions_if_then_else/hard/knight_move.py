# knight: curr (5,4) = 9
# can move: (3,3) = 6, (3,5) = 8, (4,2) = 6,
# (6,2) = 8, (7,3) = 10, (7,5) = 12,
# (4,6) = 10, (6,6) = 12
# pattern: diff of max 3 when adding both coords
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# X max of +-2, Y max of +-2
# if X is 2, then y must be 1
# if Y is 2, then x must be 1
diffX = abs(x1 - x2)
diffY = abs(y1 - y2)

if diffX == 2 and diffY == 1:
    print("YES")
elif diffX == 1 and diffY == 2:
    print("YES")
else:
    print("NO")
