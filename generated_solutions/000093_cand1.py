import sys

def solve(s):
    # Initialize variables
    ab_count = ba_count = 0
    new_string = ""

    # Count the number of occurrences of 'ab' and 'ba' in the string
    for i in range(len(s) - 1):
        if s[i:i+2] == "ab" or s[i:i+2] == "ba":
            ab_count += 1
        if s[i:i+2] == "ba" or s[i:i+2] == "ab":
            ba_count += 1

    # If the number of occurrences of 'ab' and 'ba' is equal, we can leave the string untouched
    if ab_count == ba_count:
        return s

    # Otherwise, we need to make changes to the string to make both counts equal
    for i in range(len(s)):
        if s[i] == "b":
            new_string += "a"
        else:
            new_string += "b"

    return new_string

# Read input from standard input
t = int(input())
for _ in range(t):
    # Get the string s
    s = input()

    # Print the resulting string with the minimum number of steps to make \operatorname{AB}(s) equal to \operatorname{BA}(s)
    print(solve(s))
