'''
In bowling, the player starts with 10 pins at the far end of a lane. The object is to knock all the pins down.
For this exercise, the number of pins and balls will vary. Given the number of pins N and then the number of balls K
to be rolled, followed by K pairs of numbers (one for each ball rolled), determine which pins remain standing after
all the balls have been rolled. The balls are numbered from 1 to N (inclusive) for this situation.
The subsequent number pairs, one for each K represent the start to stop (inclusive) positions of the pins that were
knocked down with each role. Print a sequence of N characters, where "I" represents a pin left standing and "."
represents a pin knocked down.
'''

'''
given number of pins n with number k of total balls
follows pairs of numbers where it represents the start and stop of pins knocked down (inclusive)
I represents a pin left standing, . represents a pin that has been knocked down

'''

n = [int(x) for x in input().split()]
pins, balls = n[0], n[1]
lane = ["I"] * pins # in python we can repeat chars by multiplication

'''
the key point here is that we have a range which is the number of balls being thrown.

then we get the left and right pins which correspond to the range of pins that have been knocked down which are 
both inclusive. 

we then iterate through that range starting from l - 1 and r to include both 8 - 10 means that pins 8,9,10 have 
been knocked down. and remember that in a list the indices work from 0 so pins 8,9,10 correspond to 7,8,9 
and for the ending right hand side thats okay because it is exclusive and so goes to 9 but for the left hand 
side we need to start from subtraction of 1 to include 7 because if given is 8, - 1 = 7 

and we accordingly set the numbers within that range inclusive to be "."
'''
for i in range(balls):
    l, r = [int(x) for x in input().split()]
    for j in range(l - 1, r):
        lane[j] = "."

print("".join(lane))