# average of all elements of a sequence ending with
# number 0

el = int(input())
avg = 0 # all el added, / count
count = 0

while el != 0:
    count += 1
    avg += el
    el = int(input())
avg = avg / count

print(avg)
