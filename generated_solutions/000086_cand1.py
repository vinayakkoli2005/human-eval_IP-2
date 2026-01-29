import math

n, m = list(map(int, input().split()))

# calculate the number of perfect sequences modulo M
num_perfect_seq = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        seq = [i, j]
        is_good = True
        for k in range(2, len(seq)):
            if seq[k-1] * seq[k] < sum(seq[:k]):
                is_good = False
                break
        if is_good:
            num_perfect_seq += 1

print(num_perfect_seq % m)
