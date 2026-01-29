import sys

s = input()
x = int(input())

l_1 = r_1 = l_2 = r_2 = None

for i in range(len(s) - 1):
    if int(s[i:i+2]) == x:
        l_1 = i
        r_1 = i + 1
        break

if l_1 is not None:
    for j in range(l_1 + 1, len(s)):
        if int(s[j-1:j+1]) == x:
            l_2 = j - 1
            r_2 = j + 1
            break

if l_1 is not None and l_2 is not None:
    print(l_1, r_1)
    print(l_2, r_2)
