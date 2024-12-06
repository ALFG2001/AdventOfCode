def check_correct(dictionary, row):
    for i in range(len(row)):
        if row[i] in dictionary:
            first_part = row[:i]
            for check_num in first_part:
                if check_num in dictionary[row[i]]:
                    return False
    return True

def correct_list(dictionary, incorrect_list):
    for i in range(1, len(incorrect_list)):
        current_element = incorrect_list[i]

        if current_element in dictionary:
            first_part = incorrect_list[:i]
            last_part = incorrect_list[i + 1:]

            for j in range(len(first_part)):
                initial_element = first_part[j]

                if initial_element in dictionary[current_element]:
                    new_list = (
                        first_part[:j] +
                        [current_element, initial_element] +
                        first_part[j + 1:] +
                        last_part
                    )

                    if not check_correct(dictionary, new_list):
                        solution = correct_list(dictionary, new_list)
                        if solution:
                            return solution
                    else:
                        return new_list

def read_instructions():
    ruleset = []
    rows = []
    dict_pages = {}
    mid_sum = 0
    mid_sum_correct = 0

    with open("2024\\D5.txt", "r") as file:
        for line in file:
            if "|" in line:
                ruleset.append(line.strip("\n"))
            elif "," in line:
                rows.append(line.strip("\n"))

    for line in ruleset:
        num_before, num_after = line.split("|")
        if num_before not in dict_pages:
            dict_pages[num_before] = [num_after]
        else:
            dict_pages[num_before].append(num_after)

    for line in rows:
        num_list = line.split(",")
        correct = check_correct(dict_pages, num_list)

        if correct:
            mid_sum += int(num_list[len(num_list) // 2])
        else:
            correct_list_result = correct_list(dict_pages, num_list)
            mid_sum_correct += int(correct_list_result[len(correct_list_result) // 2])

    print("Sum of correct rules:", mid_sum)
    print("Sum of incorrect rules:", mid_sum_correct)

import time

start_time = time.time()
read_instructions()
end_time = time.time()
print(f"{end_time - start_time:.6f} seconds")
