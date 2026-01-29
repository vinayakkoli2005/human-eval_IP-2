import sys

n, q, k = map(int, input().split())
a = list(map(int, input().split()))

# create a dictionary to store the minimum cost for each student
student_min_cost = {}

for i in range(q):
    l, r = map(int, input().split())
    
    # calculate the minimum cost for each day for this student
    min_cost = 0
    for j in range(l, r+1):
        if j in a:
            min_cost += a[j]
        else:
            min_cost += 0
    
    # update the minimum cost for this student
    if l not in student_min_cost or student_min_cost[l] > min_cost:
        student_min_cost[l] = min_cost

# output the minimum cost for each student
for key, value in sorted(student_min_cost.items()):
    print(value)
