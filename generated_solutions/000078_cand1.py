import sys

# Read the input from standard input
n, m = map(int, sys.stdin.readline().split())
tiles = []
for _ in range(n):
    tiles.append(list(map(int, sys.stdin.readline().split())))

# Convert each tile to its binary form and determine which side it has a wall on
binary_tiles = []
for tile in tiles:
    binary_tile = ""
    for i in range(m):
        if tile[i] == 0:
            binary_tile += "0"
        else:
            binary_tile += "1"
    binary_tiles.append(binary_tile)

# Determine the room sizes for each tile
room_sizes = []
for i in range(len(tiles)):
    room_size = 0
    for j in range(m):
        if binary_tiles[i][j] == "1":
            room_size += 1
    room_sizes.append(room_size)

# Sort the room sizes from biggest to smallest and print them
room_sizes = sorted(room_sizes, reverse=True)
print(*room_sizes, sep=" ")
