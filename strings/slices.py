s = str(input())

# Third character of the String
print(s[2])

# Second to last character of the String
print(s[-2])

# First five characters of the String
# The :n is exclusive, meaning it only counts up to n - 1
print(s[:5])

# All but last two characters of the String
print(s[:-2])

# Even indices only, step by 2
print(s[::2])

# Odd indices only
# Step by two starting from 1
print(s[1::2])

# Print all characters of the String in reverse order
# Do a -1 extended step which is printing in reverse order
print(s[::-1])

# Every second String in reverse order is just -2 step with extended step syntax
print(s[::-2])

# Print the length
print(len(s))