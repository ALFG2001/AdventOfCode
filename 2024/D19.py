from functools import cache

def parse(path):
    # Read data from the file
    with open(path, "r") as file:
        lines = file.readlines()
        # The first line contains patterns separated by ", "
        patterns = lines[0].strip("\n").split(", ")
        # The remaining lines contain designs, stripped of newline characters
        designs = [line.strip("\n") for line in lines[2:]]  
    return patterns, designs

def match_pattern_recursively(design, patterns):
    # If the design is completely processed, return True
    if not design:
        return True

    # Check if the design starts with any pattern
    for p in patterns:
        if design.startswith(p):
            # Try to resolve the rest of the design recursively
            if match_pattern_recursively(design[len(p):], patterns):
                return True

    # If no pattern matches, return False
    return False

@cache
def count_matching_patterns(design, patterns):
    # If the design is completely processed, return 1 (valid solution found)
    if not design:
        return 1

    total_count = 0
    # Check if the design starts with any pattern
    for p in patterns:
        if design.startswith(p):
            # Add the number of valid combinations found recursively
            total_count += count_matching_patterns(design[len(p):], patterns)

    # Return the total number of valid combinations
    return total_count

def find_patterns(designs, patterns):
    valid_patterns = 0  # Counter to store amount of designs that can be resolved
    pattern_counts = 0  # Counter to store the counts of valid combinations

    for d in designs:
        # Check if the design can be resolved using the patterns
        if match_pattern_recursively(d, patterns):
            valid_patterns += 1
            # Count the number of valid combinations for the design
            count = count_matching_patterns(d, tuple(patterns))
            pattern_counts += count

    # Return the count of valid designs and the total number of valid combinations
    return valid_patterns, pattern_counts

import time

start_time = time.time()  # Record the start time of execution

# Parse the input file to get patterns and designs
patterns, designs = parse("2024/D19.txt")

# Find the valid patterns and their total count
possible_patterns, total_patterns = find_patterns(designs, patterns)

# Print the results
print("Possible Patterns:", possible_patterns)
print("Total Patterns:", total_patterns)

end_time = time.time()  # Record the end time of execution
print(f"Execution time: {end_time - start_time:.2f} seconds")
