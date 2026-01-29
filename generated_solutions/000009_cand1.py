import math

# Read the input
n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
s = []
t = []
for _ in range(n - 1):
    s_i, t_i = list(map(int, input().split()))
    s.append(s_i)
    t.append(t_i)

# Initialize the graph
graph = {}
for i in range(1, n + 1):
    graph[i] = []
for i in range(len(s)):
    graph[s[i]].append(t[i])
    graph[t[i]].append(s[i])

# Initialize the illusion rates
illusions = {}
for i in range(1, n + 1):
    illusions[i] = a[i - 1]

# Process the queries
for _ in range(q):
    # Read the query
    type, u, v = list(map(int, input().split()))
    
    if type == 1:
        # Change the illusion rate of room u to c
        c = int(input())
        illusions[u] = c
    
    elif type == 2:
        # Calculate the minimum sum of energy needed for Chanek and Indiana to take the secret treasure at room v if they are initially at room u
        # Initialize the energy with the energy needed for them to move from the starting room to room u
        energy = abs(illusions[u]) + abs(illusions[v])
        
        # Add the energy needed for them to move through each tunnel
        for i in range(1, n + 1):
            if i != u and i != v:
                if u in graph[i] or v in graph[i]:
                    energy += max(abs(illusions[u] + illusions[i]), abs(illusions[u] - illusions[i]))
        
        # Print the minimum sum of energy needed for Chanek and Indiana to take the secret treasure at room v if they are initially at room u
        print(energy)
