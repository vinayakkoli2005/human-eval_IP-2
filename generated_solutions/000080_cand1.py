# Read input from standard input
n, *a, b = map(int, input().split())

# Initialize variables for solution
jumps = 0
depths = [0]

# Loop through the depths of the well and calculate the minimum number of jumps to reach ground level
for i in range(1, n+1):
    while depths[-1] < i:
        depths.append(depths[-1] + a[i-1])
        jumps += 1
    if depths[-1] > i:
        depths.append(depths[-1] - b[i-1])

# Print the minimum number of jumps and the sequence of depths
print(jumps)
print(*depths, sep='\n')
