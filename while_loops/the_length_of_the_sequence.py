# given a sequence of non-negative integers
# determine length of sequence where the
# sequence ends when integer == 0.
# Print length of the sequence, not counting
# the 0.

nonZero = True
counter = 0

while nonZero:
    n = int(input())
    if n > 0:
        counter += 1
    else:
        nonZero = False

print(counter)
