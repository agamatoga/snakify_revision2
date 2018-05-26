'''

Hour hand turned by α degrees since the midnight.

Determine the angle by which minute hand
turned since the start of the current hour.

Input and output in this problems are floating-point numbers.

'''

'''
We are given initially the number of degrees the hour hand has turned since midnight.

We need to determine where the minute hand is since the start of this current hour. 

We need to know how many minutes have passed since that current hour, 
which is the remaining degrees so we do total degrees % 30 which gives us remainder degrees which represents 
the minutes since the current hour. 

Once we have the degree we need to determine the angle which can be determined by multiplying the remainder degree
by 12. We multiply the minutes degree by 12 because there are 12 hours in a clock and thus, the current minute 
degree is the remainder multiplied by 12.

'''
a = float(input())

print(a % 30 * 12)