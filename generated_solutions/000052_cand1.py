import sys

# Read input from standard input
t = int(input())
for i in range(t):
    n = int(input())
    
    # Initialize variables for l and r
    l, r = 0, 1
    
    # Loop until we find a valid pair of integers
    while True:
        s = (l * (l + 1)) // 2 + (r * (r - 1)) // 2
        if s == n:
            break
        elif s > n:
            r -= 1
        else:
            l += 1
    
    # Print the answer
    print(l, r)
