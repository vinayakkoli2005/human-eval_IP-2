import sys

# Read input
n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(input()))
q = int(input())
queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))

# Initialize output
output = []

# Loop through each query
for query in queries:
    # Get the row and column indices of the subgrid
    x1, x2 = query[0], query[1]
    
    # Check if the subgrid is determinable
    determinable = True
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'X' and (i, j) not in [(i, x1-1), (i, x2+1)]:
                determinable = False
                break
        if not determinable:
            break
    output.append('YES' if determinable else 'NO')

# Print output
for line in output:
    print(line)
