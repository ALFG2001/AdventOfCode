# Function to perform multiplication of two numbers
def mul(a, b):
    return a * b

# Function to calculate the total multiplications and enabled multiplications
def calculate_multiplications():
    # Open the file "2024\\D3.txt" and read the entire content into the 'line' variable
    with open("2024\\D3.txt", "r") as file:
        line = file.read()

    # Initialize variables: 'index' to track position, 'sum_mul_part1' for all multiplications,
    # 'enabled' to track whether multiplications are enabled, and 'sum_mul_part2' for enabled multiplications
    index = 0
    sum_mul_part1 = 0
    enabled = True
    sum_mul_part2 = 0

    # Loop until no more 'do()', 'don't()', or 'mul(' are found
    while index != -1:
        # Find the next occurrences of 'do()', 'don't()', and 'mul(' starting from the current index
        do_index = line.find("do()", index)
        dont_index = line.find("don't()", index)
        mul_index = line.find("mul(", index)

        # Find the earliest occurrence of any of the three keywords
        next_index = min((i for i in [do_index, dont_index, mul_index] if i != -1), default=-1)
        if next_index == -1:
            break  # Exit loop if no more relevant keywords are found

        # Handle the occurrence of 'do()' to enable multiplication
        if next_index == do_index:
            enabled = True
            index = do_index + 4  # Move past the 'do()'

        # Handle the occurrence of 'don't()' to disable multiplication
        elif next_index == dont_index:
            enabled = False
            index = dont_index + 7  # Move past the 'don't()'

        # Handle the occurrence of 'mul(' to process a multiplication
        elif next_index == mul_index:
            start = mul_index + 4  # Start of parameters in 'mul('
            end = line.find(")", start)  # End of parameters

            if end != -1:
                # Extract the parameters and check if they are valid numbers
                params = line[start:end].split(",")
                if len(params) == 2 and all(p.strip().isdigit() for p in params):
                    # Evaluate the multiplication expression if enabled
                    if enabled:
                        sum_mul_part2 += eval(line[mul_index:end+1])  # Add to enabled sum
                    sum_mul_part1 += eval(line[mul_index:end+1])  # Always add to total sum

            index = mul_index + 4  # Move past the 'mul('

    # Output the results: total of all multiplications and total of enabled multiplications
    print("Total of the multiplications:", sum_mul_part1)
    print("Total of the enabled multiplications:", sum_mul_part2)


import time

# Measure the execution time of the function
start_time = time.time()
calculate_multiplications()
end_time = time.time()

# Print the elapsed time in seconds
print(f"{end_time - start_time:.6f} seconds")
