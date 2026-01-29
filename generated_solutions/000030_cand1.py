import sys

def main():
    # Read input
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))

        # Calculate sum of array elements
        s = sum(a)

        # Initialize count of nearly full subsequences to 0
        cnt = 0

        # Iterate over all subarrays of length n-1
        for i in range(n-1):
            # Calculate the sum of the current subarray
            curr_sum = sum(a[i:i+n-1])
            if curr_sum == s-1:
                cnt += 1

        # Print the number of nearly full subsequences
        print(cnt)

if __name__ == "__main__":
    main()
