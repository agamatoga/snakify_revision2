'''
H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
Determine the angle (in degrees) of the hour hand on the clock face right now.

'''

'''
Total clock degrees is 360. 

What we are trying to do is here is find the amount in degrees that the hour hand has moved given the 
minute, seconds and hour marker. 

First we find the degree of the hour hand marker, and every hour marker is 30 degrees.
Then, we need to see how much the hour hand marker has moved based on the minute degree marker,
and in each hour hand marker there are 60 minute markers so we need how many degrees within the hour 
degree (30) which is 30 / 60. Then, within that we need to find the amount of degrees the hour hand moves 
for every second marker. And in each minute marker there are 60 second markers thus (.5 / 60).
'''

# Every hour marker is 30 degrees 360 / 12
# Each minute marker is 1/2 degree 30 / 60, "in every hour marker, how many minute markers?"
# There are 60 minute markers in one hour, so thus the degree in minutes is 30 divided by 60
# Each second marker is .5 / 60 = (1 / 120), "in every hour marker, how many second markers?"
# In each minute marker, there are 60 second markers, meaning .5 / 60

h = int(input())
m = int(input())
s = int(input())

convertH = h * 30
convertM = m * (1/2)
convertS = s * (.5 / 60)

total = convertH + convertM + convertS

print(float(total))
