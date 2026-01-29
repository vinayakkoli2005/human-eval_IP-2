for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    
    # Initialize the robot's position and the maximum number of commands that can be executed
    x, y = 1, 1
    max_commands = 0
    
    # Iterate through the sequence of commands
    for command in s:
        if command == 'L':
            x -= 1
        elif command == 'R':
            x += 1
        elif command == 'D':
            y += 1
        elif command == 'U':
            y -= 1
        
        # If the robot falls off the board, stop executing commands
        if x < 1 or x > n or y < 1 or y > m:
            break
        
        # Increment the number of executed commands
        max_commands += 1
    
    # Print the coordinates of the cell from which the robot should start moving to execute as many commands as possible
    print(f"{x} {y}")
