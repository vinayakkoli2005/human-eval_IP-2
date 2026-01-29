import sys

def solve(n):
    # Initialize variables
    total = 0
    selected_problems = set()

    # Iterate over each problem
    for i in range(1, n+1):
        # Check if the problem is already selected
        if i not in selected_problems:
            # Add the problem to the selected problems set
            selected_problems.add(i)
            # Increment the total number of ways
            total += 1
            # Check if there are at least three problems selected
            if len(selected_problems) == 3:
                # If so, break out of the loop
                break
    return total

# Read input from standard input
t = int(input())

# Iterate over each test case
for i in range(t):
    # Read the number of problems
    n = int(input())
    # Print the number of ways to select three problems that meet either of the requirements
    print(solve(n))
