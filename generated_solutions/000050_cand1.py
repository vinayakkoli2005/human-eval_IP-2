import sys

# Read the number of test cases from standard input
t = int(input())

for i in range(t):
    # Read the number of vertices and questions for this test case
    n, q = map(int, input().split())

    # Create a dictionary to store the counts of each integer
    counts = {}

    # Read the integers written on each vertex and their parents
    for _ in range(n):
        x, y = map(int, input().split())
        counts[x] = 0
        if y != -1:
            counts[y] += 1

    # Read the questions and answer them
    for j in range(q):
        v, l, k = map(int, input().split())

        # Get the sequence of integers on the shortest path from v to the root
        sequence = []
        while v != -1:
            sequence.append(v)
            v = counts[v]

        # Remove duplicates and order by number of occurrences
        sequence = list(dict.fromkeys(sequence))
        sequence.sort(key=lambda x: counts[x], reverse=True)

        # Count the number of times each integer occurs
        occurrences = [0] * (n + 1)
        for i in range(len(sequence)):
            occurrences[sequence[i]] += 1

        # Remove integers with less than l occurrences
        for i in range(len(occurrences) - 1, -1, -1):
            if occurrences[i] < l:
                sequence.pop()

        # Replace the sequence and print the answer to the question
        if len(sequence) >= k:
            print(sequence[k - 1])
        else:
            print(-1)
