def calculate_safe_reports():
    SafeSumPart1 = 0
    SafeSumPart2 = 0

    with open("2024\\D2.txt", "r") as reports:
        for line in reports:
            levels = list(map(int, line.strip("\n").split(" ")))

            safePart1 = True
            if sorted(levels) == levels or sorted(levels, reverse=True) == levels:
                for i in range(len(levels) - 1):
                    if abs(levels[i] - levels[i + 1]) not in [1, 2, 3]:
                        safePart1 = False
                        break
            else:
                safePart1 = False

            if safePart1:
                SafeSumPart1 += 1

            for index in range(len(levels)):
                dampenedLevels = levels[0:index] + levels[index + 1:len(levels)]

                safePart2 = True
                if sorted(dampenedLevels) == dampenedLevels or sorted(dampenedLevels, reverse=True) == dampenedLevels:
                    for i in range(len(dampenedLevels) - 1):
                        if abs(dampenedLevels[i] - dampenedLevels[i + 1]) not in [1, 2, 3]:
                            safePart2 = False
                            break
                else:
                    safePart2 = False

                if safePart2:
                    SafeSumPart2 += 1
                    break

    print("Total safe reports:", SafeSumPart1)
    print("Total safe reports (dampened):", SafeSumPart2)


import time

start_time = time.time()
calculate_safe_reports()
end_time = time.time()
print(f"{end_time - start_time:.6f} seconds")
