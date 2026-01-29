import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))

# Calculate the sum of the elements in the subsequence
sum_subseq = 0
for i in range(m):
    sum_subseq += a[i] * (m * a[i])

# Calculate the sum of the elements in the subsequence without duplicates
sum_subseq_no_duplicates = 0
for i in range(m):
    for j in range(i+1, m):
        if a[i] == a[j]:
            continue
        else:
            sum_subseq_no_duplicates += a[i] * (a[j])

# Calculate the difference between the two sums
diff = sum_subseq - sum_subseq_no_duplicates

print(diff)
