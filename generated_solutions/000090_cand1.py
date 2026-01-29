for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Check if it's possible to erase the whole sequence
    for i in range(1, len(a) + 1):
        if a[i - 1] % (i + 1) == 0:
            print("YES")
            break
    else:
        print("NO")
