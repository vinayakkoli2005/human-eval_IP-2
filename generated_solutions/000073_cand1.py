import sys

def find_enemy_fortress(grid):
    # Initialize the device's position to a random square inside the grid
    device_x = 2
    device_y = 2

    # Loop through each query and update the device's position
    for _ in range(40):
        query = input()
        if query == "!":
            # If we receive a '!' character, we have found the enemy base
            break
        else:
            x, y = map(int, query.split())
            manhattan_distance = abs(x - device_x) + abs(y - device_y)
            if manhattan_distance == 1:
                # If we are one step away from the enemy base, place the device there
                device_x = x
                device_y = y
            else:
                # Otherwise, move the device one step closer to the enemy base
                if abs(device_x - x) == 1 or abs(device_y - y) == 1:
                    # If we are already one step away from the enemy base in the same row or column as the current square, do not move
                    pass
                elif device_x > x:
                    # If we are to the left of the current square, move one step to the right
                    device_x += 1
                elif device_x < x:
                    # If we are to the right of the current square, move one step to the left
                    device_x -= 1
                elif device_y > y:
                    # If we are above the current square, move one step down
                    device_y += 1
                else:
                    # If we are below the current square, move one step up
                    device_y -= 1

    # Print the coordinates of the square inside the enemy base with the smallest x and y coordinates
    print(f"! {device_x} {device_y}")

if __name__ == "__main__":
    grid = [[0 for _ in range(10**9)] for _ in range(10**9)]
    find_enemy_fortress(grid)
