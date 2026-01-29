import sys

read_int = lambda: int(sys.stdin.readline())
read_list_int = lambda: list(map(int, sys.stdin.readline().split()))

def solve():
    n = read_int()
    tasks = []
    for _ in range(n):
        a, b = read_list_int()
        tasks.append((a, b))
    
    s = set(read_list_int())
    
    time = 0
    count = 0
    while True:
        for i, (a, b) in enumerate(tasks):
            if a <= time and b > time and i + 1 in s:
                count += 1
                time = a
        
        if len(s) == len(tasks) - sum(i + 1 not in s for i, (a, b) in enumerate(tasks)):
            break
        
        for i, (a, b) in enumerate(tasks):
            if a <= time and b > time and i + 1 not in s:
                count += 1
                time = a
    
    return count % (10**9 + 7)

print(solve())
