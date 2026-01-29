import sys

def solve(A1, A2):
    N = len(A1)
    Q = int(input())
    for _ in range(Q):
        query_type = int(input())
        if query_type == 1:
            l, r, x = map(int, input().split())
            for i in range(l-1, r+1):
                A2[i] = min(A2[i], x)
        elif query_type == 2:
            l, r, x = map(int, input().split())
            for i in range(l-1, r+1):
                A2[i] = max(A2[i], x)
        elif query_type == 3:
            l, r, x = map(int, input().split())
            for i in range(l-1, r+1):
                A2[i] += x
        else:
            l, r = map(int, input().split())
            result = 0
            for i in range(l-1, r+1):
                result += (A1[i] + A2[i]) % 10**9 + 7
            print(result)

if __name__ == "__main__":
    N = int(input())
    A1 = list(map(int, input().split()))
    A2 = list(map(int, input().split()))
    solve(A1, A2)
