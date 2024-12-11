from functools import cache

with open("2024/D11.txt", "r") as file:
    stones = [int(s) for s in file.read().strip().split()]

def blink(number):
    if number == 0:
        return [1]
    s = f'{number}'
    l = len(s)
    if l % 2 == 0:
        return [int(n) for n in [s[:l//2], s[l//2:]]]
    return [number * 2024]

@cache
def count_splits(number, blinks):
    if blinks == 0:
        return 1
    return sum(count_splits(n, blinks - 1) for n in blink(number))

def dayEleven():
    parte1 = 0
    parte2 = 0
    for stone in stones:
        parte1 += count_splits(stone, 25)
        parte2 += count_splits(stone, 75)

    print("p1:", parte1)
    print("p2:", parte2)

# Measure execution time
import time

start_time = time.time()  # Start the timer
dayEleven()  # Call the function
end_time = time.time()  # End the timer
print(f"{end_time - start_time:.6f} seconds")  # Print the execution time

