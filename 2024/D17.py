# Open and read the file
with open("2024/D17.txt") as f:
    lines = f.readlines()

# Parse the first three lines as integers for a, b, and c
a = int(lines[0].split(":")[1].strip())  # Extract 'a' from the first line
b = int(lines[1].split(":")[1].strip())  # Extract 'b' from the second line
c = int(lines[2].split(":")[1].strip())  # Extract 'c' from the third line

# Parse the program from the fifth line
prog = [int(n) for n in lines[4].strip().split(" ")[1].split(",")]

def run(prog, a):
    """
    Runs the program given a starting value of 'a'.
    
    The program consists of a series of operations where each operation modifies 
    the value of 'a', 'b', or 'c' or performs other control flow actions.
    """
    ip, b, c, out = 0, 0, 0, []  # Initialize instruction pointer (ip), and variables b, c, and output list
    while ip >= 0 and ip < len(prog):  # Loop through the program instructions
        # Determine the value of combo based on the current instruction
        lit, combo = prog[ip+1], [0, 1, 2, 3, a, b, c, 99999][prog[ip+1]]
        
        match prog[ip]:
            case 0:  # adv: Update 'a' by dividing it by 2 raised to the power of combo
                a = int(a / 2**combo)
            case 1:  # bxl: Perform bitwise XOR between 'b' and lit
                b = b ^ lit
            case 2:  # bst: Set 'b' to combo modulo 8
                b = combo % 8
            case 3:  # jnz: Jump to a specific instruction if 'a' is non-zero
                ip = ip if a == 0 else lit - 2
            case 4:  # bxc: Perform bitwise XOR between 'b' and 'c'
                b = b ^ c
            case 5:  # out: Append combo modulo 8 to the output list
                out.append(combo % 8)
            case 6:  # bdv: Set 'b' to 'a' divided by 2 raised to the power of combo
                b = int(a / 2**combo)
            case 7:  # cdv: Set 'c' to 'a' divided by 2 raised to the power of combo
                c = int(a / 2**combo)
        
        ip += 2  # Move to the next instruction
    return out  # Return the output generated during execution

# Print the output of part 1
print("Part 1:", ",".join(str(n) for n in run(prog, a)))

# Reverse the program for part 2 and try to find the starting 'a' that leads to the target output
target = prog[::-1]

def find_a(a=0, depth=0):
    """
    Recursively finds the starting value of 'a' that leads to the target output.
    
    The function tries all combinations of 'a' and calls the run function to check 
    if the output matches the target at the current depth.
    """
    if depth == len(target):  # Base case: If depth equals the length of target, return 'a'
        return a
    
    # Try all possible values for 'i' and check if the output matches the target at the current depth
    for i in range(8):
        output = run(prog, a * 8 + i)  # Run the program with the current 'a' multiplied by 8 and adding 'i'
        if output and output[0] == target[depth]:  # Check if output matches the target at current depth
            # Recursively search for the correct 'a'
            if result := find_a(a * 8 + i, depth + 1):
                return result  # Return the result if found
    return 0  # Return 0 if no match is found

# Print the result for part 2
print("Part 2:", find_a())
