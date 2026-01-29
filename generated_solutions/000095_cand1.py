import sys

def get_min_banknote(n, k):
    burles = 0
    count = 0
    for i in range(1, n+1):
        while burles + i <= k:
            burles += i
            count += 1
    return count

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_min_banknote(n, k))
