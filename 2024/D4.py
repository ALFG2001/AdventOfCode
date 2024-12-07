# Function to find occurrences of 'XMAS' and 'MAS' cross in the grid
def find(letters, word):
    # Possible directions to check for the word (horizontal, vertical, and diagonal)
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)
    ]
    word_len = len(word)
    count_xmas = 0  # To count occurrences of 'XMAS'
    count_cross = 0  # To count occurrences of 'MAS' cross

    # Function to check if the 'MAS' cross exists around a given cell
    def check_x_mas(i, j):
        # Ensure that the check stays within bounds of the grid
        if not (0 <= i - 1 < len(letters) and 0 <= i + 1 < len(letters) and 
                0 <= j - 1 < len(letters[0]) and 0 <= j + 1 < len(letters[0])):
            return False

        # Check if the current cell is 'A' (part of 'XMAS' or 'MAS')
        if letters[i][j] != 'A':
            return False

        # Define the four cases where 'MAS' forms a cross around 'A'
        case1 = (
            letters[i - 1][j - 1] == 'S' and letters[i - 1][j + 1] == 'M' and
            letters[i + 1][j - 1] == 'S' and letters[i + 1][j + 1] == 'M'
        )
        case2 = (
            letters[i - 1][j - 1] == 'S' and letters[i - 1][j + 1] == 'S' and
            letters[i + 1][j - 1] == 'M' and letters[i + 1][j + 1] == 'M'
        )
        case3 = (
            letters[i - 1][j - 1] == 'M' and letters[i - 1][j + 1] == 'S' and
            letters[i + 1][j - 1] == 'M' and letters[i + 1][j + 1] == 'S'
        )
        case4 = (
            letters[i - 1][j - 1] == 'M' and letters[i - 1][j + 1] == 'M' and
            letters[i + 1][j - 1] == 'S' and letters[i + 1][j + 1] == 'S'
        )

        # Return True if any of the cross patterns match
        return case1 or case2 or case3 or case4

    # Iterate through the grid to check for word and cross patterns
    for i in range(len(letters)):
        for j in range(len(letters[i])):
            # Check for 'MAS' cross at each cell
            if check_x_mas(i, j):
                count_cross += 1
            # Check for 'XMAS' occurrences in all directions
            for dx, dy in directions:
                # Check if the word fits in the grid in the given direction
                if all(
                    0 <= i + k * dx < len(letters) and
                    0 <= j + k * dy < len(letters[0]) and
                    letters[i + k * dx][j + k * dy] == word[k]
                    for k in range(word_len)
                ):
                    count_xmas += 1

    # Return the counts of 'XMAS' occurrences and 'MAS' crosses
    return count_xmas, count_cross

# Function to calculate the occurrences of 'XMAS' and 'MAS' cross in a grid
def calculate_occurrences():
    letters = []
    # Read the grid of letters from the file
    with open("2024\\D4.txt", "r") as file:
        for line in file:
            letters.append([l for l in line.strip("\n")])

    word = "XMAS"  # The word we are looking for
    count_xmas, count_cross = find(letters, word)  # Call the find function

    # Print the results
    print(f"The word '{word}' appears {count_xmas} times.")
    print(f"The 'MAS' cross appears {count_cross} times.")

import time

# Measure the execution time of the function
start_time = time.time()
calculate_occurrences()
end_time = time.time()

# Print the elapsed time in seconds
print(f"{end_time - start_time:.6f} seconds")
