t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # initialize the max_min variable to infinity
    max_min = float('inf')
    
    # loop through each element of the array and find the minimum value
    for i in range(n):
        if a[i] < max_min:
            max_min = a[i]
    
    print(max_min)
