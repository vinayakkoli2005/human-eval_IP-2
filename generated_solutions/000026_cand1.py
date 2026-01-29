import math

def main():
    n, m = map(int, input().split())
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(i, n):
            if a[i] + a[j] < m:
                dp[a[i] + a[j]] += 1
    return sum(dp) % 998244353

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    print(main())
