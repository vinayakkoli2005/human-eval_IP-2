import sys

# read input
t = int(input())
test_cases = []
for _ in range(t):
    test_cases.append(input().split())

# solve test cases
results = []
for i, case in enumerate(test_cases):
    keyboard = case[0]
    word = case[1]
    result = 0
    for c in word:
        position = keyboard.index(c)
        if i > 0 and position < test_cases[i-1][0].index(word[0]):
            result += abs(position - test_cases[i-1][0].index(word[0]))
    results.append(result)

# print output
for result in results:
    print(result)
