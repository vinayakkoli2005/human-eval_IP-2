import sys

# read input
t = int(input())
for case in range(t):
    n, k = map(int, input().split())
    
    # find minimum number of hours required
    min_hours = (n - 1) // k + 1
    
    # output answer
    print(min_hours)
