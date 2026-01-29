import sys

def solve(n, m, rectangle):
    # Initialize variables
    operations = 0
    portal_found = False

    # Iterate through each row and column of the rectangle
    for i in range(n):
        for j in range(m):
            # If the current block is an obsidian block and it is not a corner, increment operations
            if rectangle[i][j] == "1" and (i != 0 or j != 0) and (i != n - 1 or j != m - 1):
                operations += 1

    # If no portal was found, return the number of operations
    if not portal_found:
        return operations

    # Otherwise, iterate through each row and column of the rectangle again
    for i in range(n):
        for j in range(m):
            # If the current block is an obsidian block and it is a corner, set portal_found to True
            if rectangle[i][j] == "1" and (i == 0 or j == 0) or (i == n - 1 or j == m - 1):
                portal_found = True

    # Return the number of operations plus the number of times the loop iterated through the rectangle to find the portal
    return operations + 1

# Read input from standard input
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read the dimensions of the rectangle and the rectangle itself from standard input
    n, m = map(int, input().split())
    rectangle = []
    for _ in range(n):
        rectangle.append(input())

    # Call the solve function with the dimensions and the rectangle to get the minimum number of operations needed to make at least one sub-rectangle a portal
    print(solve(n, m, rectangle))
