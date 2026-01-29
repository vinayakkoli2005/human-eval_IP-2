import sys

# Read input from standard input
read_stdin = lambda: sys.stdin.readline().strip()

# Main function to read test cases and solve the problem
def main():
    # Number of test cases
    t = int(read_stdin())
    
    for i in range(t):
        # Read number of cards, starting indices, and directions
        n, a, b = map(int, read_stdin().split())
        da, db = read_stdin().split()
        
        # Initialize the array of card numbers
        cards = [i for i in range(n)]
        
        # Initialize the starting indices and directions
        start_a = a % n
        start_b = b % n
        dir_a = da == "left"
        dir_b = db == "left"
        
        # Initialize the current index of card A and B
        cur_a = start_a
        cur_b = start_b
        
        # Initialize the direction of movement for card A and B
        move_a = dir_a
        move_b = dir_b
        
        # Loop until only one card remains
        while len(cards) > 1:
            # Move card A and update its position
            if move_a:
                cur_a = (cur_a + 1) % n
            else:
                cur_a = (cur_a - 1) % n
            
            # Mark the current card for removal if it is already in a cycle
            if cards[cur_a] in cards[:cur_a] or cards[cur_a] in cards[cur_a+1:]:
                cards.remove(cards[cur_a])
            
            # Update the direction of movement for card A
            move_a = not dir_a if cur_a == start_a else dir_a
            
            # Move card B and update its position
            if move_b:
                cur_b = (cur_b + 1) % n
            else:
                cur_b = (cur_b - 1) % n
            
            # Mark the current card for removal if it is already in a cycle
            if cards[cur_b] in cards[:cur_b] or cards[cur_b] in cards[cur_b+1:]:
                cards.remove(cards[cur_b])
            
            # Update the direction of movement for card B
            move_b = not dir_b if cur_b == start_b else dir_b
        
        # Print the index of the last remaining card
        print(cards[0])

# Call the main function to read and solve the problem
if __name__ == "__main__":
    main()
