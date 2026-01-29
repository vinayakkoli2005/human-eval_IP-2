import sys

def solve(a, n):
    # Calculate the sum of extreme values of all nonempty subarrays of a modulo 998244353
    # using the given algorithm
    sum_extreme = 0
    for i in range(n):
        for j in range(i, n):
            subarray = a[i:j+1]
            if len(subarray) == 0:
                continue
            if subarray == sorted(subarray):
                sum_extreme += 0
            else:
                min_value = sys.maxsize
                for k in range(len(subarray)):
                    for l in range(k, len(subarray)):
                        value = subarray[l] - subarray[k]
                        if value < min_value and value > 0:
                            min_value = value
                sum_extreme += min_value % 998244353
    return sum_extreme

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a, n))
