# Read the input from standard input
n, m = map(int, input().split())
a = input()
b = input()

# Initialize the minimum number of elements to change for each k value
min_changes = {}
for i in range(n - m + 1):
    min_changes[i] = float('inf')

# For each possible value of k, find the minimum number of elements to change
# such that there are exactly k occurrences of b as a substring in a
for k in range(n - m + 1):
    # Initialize the number of changes to 0
    num_changes = 0
    
    # Iterate through the characters of a and check if they match b
    for i in range(len(a)):
        j = i
        while j < len(a) and b == a[i:j+m]:
            # If a substring of b is found, increment the number of changes
            num_changes += 1
            j += m
    
    # Update the minimum number of elements to change for this value of k
    min_changes[k] = min(num_changes, min_changes[k])

# Output the minimum number of elements to change for each k value
for i in range(n - m + 1):
    print(min_changes[i], end=' ')
