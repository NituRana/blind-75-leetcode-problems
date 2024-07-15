'''
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits
it has (also known as the Hamming weight).


Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

'''
def count_set_bits(binary_str):
    # Convert binary string to integer
    num = int(binary_str, 2)
    
    # Initialize a counter for set bits
    count = 0
    
    # Loop through each bit using bitwise operations
    while num > 0:
        count += num & 1  # Add 1 to count if the least significant bit is set
        num >>= 1         # Right shift the number to check the next bit
    
    return count

# Example usage:
binary_representation = bin(128)
number_of_set_bits = count_set_bits(binary_representation)

print("------------------- number_of_set_bits :", number_of_set_bits)

