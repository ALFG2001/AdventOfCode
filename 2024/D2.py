def calculate_safe_reports():
    # Initialize variables to store the total count of safe reports
    SafeSumPart1 = 0
    SafeSumPart2 = 0

    # Open the file "2024\\D2.txt" in read mode to process each report
    with open("2024\\D2.txt", "r") as reports:
        for line in reports:
            # Split the line into integers, representing the levels of the report
            levels = list(map(int, line.strip("\n").split(" ")))

            # Part 1: Check if the levels are in a safe order (either ascending or descending)
            safePart1 = True
            if sorted(levels) == levels or sorted(levels, reverse=True) == levels:
                # Check if the differences between consecutive levels are 1, 2, or 3
                for i in range(len(levels) - 1):
                    if abs(levels[i] - levels[i + 1]) not in [1, 2, 3]:
                        safePart1 = False
                        break
            else:
                safePart1 = False

            # If Part 1 conditions are met, increment the SafeSumPart1 counter
            if safePart1:
                SafeSumPart1 += 1

            # Part 2: Check if removing one level results in a safe order
            for index in range(len(levels)):
                # Create a new list by removing the current level
                dampenedLevels = levels[0:index] + levels[index + 1:len(levels)]

                safePart2 = True
                # Check if the remaining levels are either in ascending or descending order
                if sorted(dampenedLevels) == dampenedLevels or sorted(dampenedLevels, reverse=True) == dampenedLevels:
                    # Check if the differences between consecutive levels are 1, 2, or 3
                    for i in range(len(dampenedLevels) - 1):
                        if abs(dampenedLevels[i] - dampenedLevels[i + 1]) not in [1, 2, 3]:
                            safePart2 = False
                            break
                else:
                    safePart2 = False

                # If Part 2 conditions are met, increment the SafeSumPart2 counter and break from the loop
                if safePart2:
                    SafeSumPart2 += 1
                    break

    # Output the total safe reports for both Part 1 and Part 2
    print("Total safe reports:", SafeSumPart1)
    print("Total safe reports (dampened):", SafeSumPart2)


import time

# Measure the execution time of the function
start_time = time.time()
calculate_safe_reports()
end_time = time.time()

# Print the elapsed time in seconds
print(f"{end_time - start_time:.6f} seconds")
