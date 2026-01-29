import math

N, Q = map(int, input().split())

cities = list(map(int, input().split()))
queries = []

for i in range(Q):
    L, R, D = map(int, input().split())
    queries.append((L-1, R-1, D))

def check_road(start, end, length):
    if start == end:
        return True
    
    for i in range(start+1, end+1):
        if cities[i] - cities[start] == length or cities[end] - cities[i] == length:
            return check_road(i, end, length)
        
    return False

for i in range(Q):
    L, R, D = queries[i]
    if check_road(L, R, D):
        print("Yes")
    else:
        print("No")
