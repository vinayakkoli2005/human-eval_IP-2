import sys

def largest_composite_subset(arr):
    # Find the largest subset with composite sum
    max_size = 0
    max_sum = 0
    for i in range(len(arr)):
        sum = 1
        for j in range(i+1, len(arr)):
            sum *= arr[j]
            if sum % (j-i+1) == 0:
                break
        if sum > max_sum:
            max_sum = sum
            max_size = j - i + 1
    return max_size, arr[i:i+max_size]

# Read from standard input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    # Find the largest subset with composite sum
    size, subset = largest_composite_subset(arr)
    
    # Output the result
    print(size)
    print(*subset, sep=' ')
