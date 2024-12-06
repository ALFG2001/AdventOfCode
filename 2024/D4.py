def find(letters, word):
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)
    ]
    word_len = len(word)
    count_xmas = 0
    count_cross = 0

    def check_x_mas(i, j):
        if not (0 <= i - 1 < len(letters) and 0 <= i + 1 < len(letters) and 
                0 <= j - 1 < len(letters[0]) and 0 <= j + 1 < len(letters[0])):
            return False

        if letters[i][j] != 'A':
            return False

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

        return case1 or case2 or case3 or case4

    for i in range(len(letters)):
        for j in range(len(letters[i])):
            if check_x_mas(i, j):
                count_cross += 1
            for dx, dy in directions:
                if all(
                    0 <= i + k * dx < len(letters) and
                    0 <= j + k * dy < len(letters[0]) and
                    letters[i + k * dx][j + k * dy] == word[k]
                    for k in range(word_len)
                ):
                    count_xmas += 1

    return count_xmas, count_cross

def calculate_occurrences():
    letters = []
    with open("2024\\D4.txt", "r") as file:
        for line in file:
            letters.append([l for l in line.strip("\n")])

    word = "XMAS"
    count_xmas, count_cross = find(letters, word)

    print(f"The word '{word}' appears {count_xmas} times.")
    print(f"The 'MAS' cross appears {count_cross} times.")

import time

start_time = time.time()
calculate_occurrences()
end_time = time.time()
print(f"{end_time - start_time:.6f} seconds")
