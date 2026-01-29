# Read input
t = int(input())

for case in range(t):
    # Read number of people and their sociability
    n = int(input())
    a = list(map(int, input().split()))

    # Initialize talks array with 0s
    talks = [0] * n

    # Find the maximum number of talks possible
    max_talks = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] <= max_talks:
                break
            elif a[i] >= a[j]:
                talks[i] += 1
                talks[j] += 1
                max_talks += 2
    print(max_talks)
    for i in range(n):
        if talks[i] > 0:
            print(i+1, (i+1)%n+1)
