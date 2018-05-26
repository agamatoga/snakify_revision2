a = input().split() # get the input of numbers and split it based on whitespace which is the default

# then print all the even indices by using the "step" functionality in python

for i in range(0,len(a),2):
    print(a[i])

# remember that even + even is always even! 