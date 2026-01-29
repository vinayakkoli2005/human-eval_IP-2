import sys

n = int(sys.stdin.readline())
grid = []
for i in range(n):
	grid.append([])
	line = sys.stdin.readline()
	for j in range(n):
		grid[i].append(line[j])
		
#print(grid)
colors = set()
# Check for color uniqueness 
if len(set([grid[i][j] for i in range(n) for j in range(n)])) == n * n:
	print('UNIQUE')
else: 
	print('NONE')
# Check if there is a way to make a mastapeece 
if len([i for i in range(n) if grid[i][j] == 'S' or grid[i][j] == 'G']) > 1 and all(len([k for k in range(n) if grid[k][j] == grid[i][j]]) == 2 for j in range(n)):
	for i in range(n):
		print(grid[i])
else:
	print('NONE')
