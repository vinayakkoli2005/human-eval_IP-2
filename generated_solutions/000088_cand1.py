import sys

def solve(a):
    n = len(a)
    count = 0
    for i in range(1, n+1):
        if a[i-1] > i:
            count += 1
    return count

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))
