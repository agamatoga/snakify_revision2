'''
Given a list of numbers, find and print all the elements that are greater than the previous element.
'''

'''
so what we want to do is iterate over all the elements in a list.
and only print those that are greater than the previous i.e. those at i + 1 index where i + 1 > i 

the problem we had initially is the input is given as a String and Python implicit conversions don't always 
work the way we want it to. So be safe and always explicitly convert things in Python! 
'''


li = [int(x) for x in input().split()]

for i in range(0, len(li)):
    if i > 0:
        if li[i] > li[i - 1]:
            print(li[i])