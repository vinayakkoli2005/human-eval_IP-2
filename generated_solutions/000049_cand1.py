import sys

def solve(a):
    # Sort the array in non-decreasing order using only 3-cycles
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[j] < a[i]:
                # Swap elements at indices i and j
                a[i], a[j] = a[j], a[i]
                break
    return a

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Print output
    if solve(a) == sorted(a):
        print("YES")
    else:
        print("NO")
