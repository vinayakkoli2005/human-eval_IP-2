import math

def solve(k):
    mod = 10**9 + 7
    num_nodes = 2**k - 1
    num_good_colorings = 0
    
    # Initialize the good coloring counts for each node
    node_counts = [0] * (num_nodes + 1)
    
    # Loop through all possible color combinations
    for i in range(2**k):
        # Get the binary representation of the current color combination
        bin_str = bin(i)[2:]
        bin_str = '0' * (k - len(bin_str)) + bin_str
        
        # Check if the color combination is valid
        valid = True
        for j in range(k):
            if bin_str[j] == '1':
                if bin_str[j-1] == '1' or bin_str[j+1] == '1':
                    valid = False
                    break
        
        # If the color combination is valid, increment the good coloring count for each node
        if valid:
            for j in range(num_nodes + 1):
                if bin_str[j]:
                    node_counts[j] += 1
    
    # Calculate the number of different colorings by dividing the good coloring counts by the total number of nodes
    for i in range(num_nodes + 1):
        num_good_colorings = (num_good_colorings * node_counts[i]) % mod
    
    return num_good_colorings

if __name__ == "__main__":
    k = int(input())
    print(solve(k) % 10**9 + 7)
