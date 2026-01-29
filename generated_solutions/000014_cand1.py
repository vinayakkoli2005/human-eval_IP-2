t = int(input())
for i in range(t):
    s = input()
    if len(s) == 0:
        print("YES")
    else:
        flag = False
        for j in range(len(s)-1):
            if s[j] == 'A' and s[j+1] == 'B':
                s = s[:j] + s[j+2:]
                flag = True
                break
        if not flag:
            for j in range(len(s)-1):
                if s[j] == 'B' and s[j+1] == 'C':
                    s = s[:j] + s[j+2:]
                    break
        print("YES" if len(s) == 0 else "NO")
