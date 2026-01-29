for _ in range(int(input())):
    n, m, k = map(int, input().split())
    field = []
    for i in range(n):
        row = input()
        field.append([c == '*' for c in row])
    
    # check if the field can be obtained by drawing ticks of size k or larger
    for i in range(n-k+1):
        for j in range(m-k+1):
            if all(field[i+d][j+d] for d in range(k)):
                print("YES")
                break
        else:
            print("NO")
            break
