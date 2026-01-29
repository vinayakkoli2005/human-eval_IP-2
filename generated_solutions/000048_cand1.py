import sys

def solve(n, k, x):
    # Sort the coordinates in ascending order
    x.sort()
    
    # Initialize the minimum distance to infinity
    min_dist = float('inf')
    
    # Loop through each pair of depots and calculate the distance between them
    for i in range(n-1):
        dist = abs(x[i+1] - x[i])
        
        # If the distance is less than the current minimum, update the minimum distance
        if dist < min_dist:
            min_dist = dist
    
    return min_dist

# Read input from standard input
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    
    # Calculate the minimum distance to deliver all bags of goods to the depots
    dist = solve(n, k, x)
    
    # Output the minimum distance
    print(dist)
