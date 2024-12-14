import numpy as np

# Open the file containing prize data
with open("2024/D13.txt", "r") as file:
    lines = file.read().split("\n")
    prizes = []
    
    # Read every 4th line and store the prize data
    for i in range(0, len(lines), 4):
        prizes.append([lines[i], lines[i+1], lines[i+2]])

# Function to extract the x and y values from a string
def readString(string, sep):
    data = string.split(":")[1].strip()
    parts = data.split(", ")

    # Extract x and y coordinates
    x = int(parts[0].split(sep)[1])
    y = int(parts[1].split(sep)[1])
    return x, y

# Function to calculate the button presses needed to reach a target position
def calculateMoves(x1, x2, y1, y2, targetX, targetY, tolerance=1e-2):
    A = np.array([[x1, x2],
                  [y1, y2]])

    b = np.array([targetX, targetY])

    # Solve the system of equations
    x, y = np.linalg.solve(A, b)

    # If the solution is close to an integer, return the rounded values
    if abs(x - round(x)) < tolerance and abs(y - round(y)) < tolerance:
        return round(x), round(y)
    else:
        return None, None

# Function to calculate the tokens
def calculateTokens():
    tokens1 = 0
    tokens2 = 0

    # Iterate over each prize and calculate the number of tokens
    for claw in prizes:
        for i, row in enumerate(claw):
            match i:
                case 0:
                    x1, y1 = readString(row, "+")
                case 1:
                    x2, y2 = readString(row, "+")
                case 2:
                    tx, ty = readString(row, "=")

        # Calculate the button presses needed for the first target position
        buttonA, buttonB = calculateMoves(x1, x2, y1, y2, tx, ty)
        if buttonA is not None or buttonB is not None:
            tokens1 += buttonA * 3 + buttonB

        # Calculate the button presses needed for the second target position
        buttonA, buttonB = calculateMoves(x1, x2, y1, y2, tx + 10000000000000, ty + 10000000000000)
        if buttonA is not None or buttonB is not None:
            tokens2 += buttonA * 3 + buttonB

    # Print the total number of tokens for each player
    print("Number of tokens p1:", tokens1)
    print("Number of tokens p2:", tokens2)


# Measure execution time
import time

start_time = time.time()  # Start the timer
calculateTokens()  # Call the function
end_time = time.time()  # End the timer
print(f"{end_time - start_time:.6f} seconds")  # Print the execution time
