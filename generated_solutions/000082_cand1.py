# Read input from standard input
n, d = map(int, input().split())
skills_and_neatnesses = []
for _ in range(n):
    skills_and_neatnesses.append(list(map(int, input().split())))

# Initialize variables for optimal climbing order and alpinist's skill level
max_num_climbers = 0
curr_difficulty = d
alpinists = []
for i in range(n):
    alpinist = {
        'skill': skills_and_neatnesses[i][0],
        'neatness': skills_and_neatnesses[i][1]
    }
    if curr_difficulty <= alpinist['skill']:
        max_num_climbers += 1
    alpinists.append(alpinist)

# Iterate through all possible climbing orders to find the maximum number of climbers
for i in range(n):
    curr_difficulty = d
    num_climbers = 0
    for j in range(i, n):
        if alpinists[j]['skill'] >= curr_difficulty:
            num_climbers += 1
            curr_difficulty = max(curr_difficulty, alpinists[j]['neatness'])
    if num_climbers > max_num_climbers:
        max_num_climbers = num_climbers

# Output the maximum number of climbers who can reach the top
print(max_num_climbers)
