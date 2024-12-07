# Function to check if a given list (row) is correct based on the dictionary of rules
def check_correct(dictionary, row):
    for i in range(len(row)):
        # Check if the current element exists in the dictionary
        if row[i] in dictionary:
            # Create the first part of the list (before the current element)
            first_part = row[:i]
            # For each element in the first part, check if it exists in the current element's list in the dictionary
            for check_num in first_part:
                if check_num in dictionary[row[i]]:
                    return False  # If it does, the list is incorrect
    return True  # If no issues were found, the list is correct

# Function to try to correct an incorrect list using the dictionary of rules
def correct_list(dictionary, incorrect_list):
    # Iterate through the list starting from the second element
    for i in range(1, len(incorrect_list)):
        current_element = incorrect_list[i]

        if current_element in dictionary:
            first_part = incorrect_list[:i]
            last_part = incorrect_list[i + 1:]

            # Iterate through the first part of the list to find possible swaps
            for j in range(len(first_part)):
                initial_element = first_part[j]

                # If swapping the elements might fix the list
                if initial_element in dictionary[current_element]:
                    # Create a new list with the swapped elements
                    new_list = (
                        first_part[:j] +
                        [current_element, initial_element] +
                        first_part[j + 1:] +
                        last_part
                    )

                    # Check if the new list is correct
                    if not check_correct(dictionary, new_list):
                        # If not correct, recursively attempt to correct it further
                        solution = correct_list(dictionary, new_list)
                        if solution:
                            return solution  # Return the corrected list
                    else:
                        return new_list  # If correct, return the new list

# Function to read the instructions from the file and process the data
def read_instructions():
    ruleset = []  # To store the rules in 'num_before | num_after' format
    rows = []  # To store the rows that need to be checked
    dict_pages = {}  # To store the dictionary mapping 'num_before' to 'num_after' pages
    mid_sum = 0  # Sum of the mid values of correct lists
    mid_sum_correct = 0  # Sum of the mid values of corrected lists

    # Read the input file
    with open("2024\\D5.txt", "r") as file:
        for line in file:
            # Split the rules by '|'
            if "|" in line:
                ruleset.append(line.strip("\n"))
            # Split the rows by ',' (numbers are separated by commas)
            elif "," in line:
                rows.append(line.strip("\n"))

    # Process the rules and create the dictionary
    for line in ruleset:
        num_before, num_after = line.split("|")
        if num_before not in dict_pages:
            dict_pages[num_before] = [num_after]  # Add num_after to the list for num_before
        else:
            dict_pages[num_before].append(num_after)

    # Process each row and check its correctness
    for line in rows:
        num_list = line.split(",")  # Split the row into individual numbers
        correct = check_correct(dict_pages, num_list)  # Check if the row is correct

        if correct:
            mid_sum += int(num_list[len(num_list) // 2])  # Add the middle element if the row is correct
        else:
            # If the row is incorrect, try to correct it and add the middle element of the corrected list
            correct_list_result = correct_list(dict_pages, num_list)
            mid_sum_correct += int(correct_list_result[len(correct_list_result) // 2])

    # Print the results
    print("Sum of correct rules:", mid_sum)
    print("Sum of incorrect rules:", mid_sum_correct)

import time

# Measure the execution time of the read_instructions function
start_time = time.time()
read_instructions()
end_time = time.time()

# Print the elapsed time in seconds
print(f"{end_time - start_time:.6f} seconds")
