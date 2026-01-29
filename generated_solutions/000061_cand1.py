import sys

# Read input
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Calculate the mean of the array
    mean = sum(a) / len(a)
    
    # Initialize variables to keep track of pairs
    pairs = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (sum(a[:i]) + sum(a[j:])) / (n - 2) == mean:
                pairs += 1
    
    results.append(pairs)

# Output the result
for result in results:
    print(result)
