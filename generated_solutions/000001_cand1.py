import sys

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

# sort the strings ascendingly and descendingly based on the first letter
s_asc = sorted(s, key=lambda x: (x[0], -ord(x[0])))
s_desc = sorted(s, key=lambda x: (-x[0], ord(x[0])))

# merge the ascending and descending lists into one list of pairs
result = []
for i in range(n):
    result.append((s_asc[i], s_desc[i]))

# output the indices of the sorted strings
output = []
for i in range(n):
    output.append(result[i][0])
    output.append(result[i][1])
print(*output, sep='\n')
