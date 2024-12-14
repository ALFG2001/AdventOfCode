# Function to create the grid (2D array) with specified width and height
def createGrid(robots, width, height):
    grid = []
    
    # Initialize a grid filled with zeros
    for y in range(height):
        row = []
        for x in range(width):
            row.append(0)  # Add 0 to each cell of the row
        grid.append(row)  # Add the row to the grid

    # Place robots on the grid based on their positions
    for robot in robots:
        # Calculate the position on the grid, ensuring it wraps around if out of bounds
        x, y = robot[0][0] % width, robot[0][1] % height
        
        # Update the cell with the number of robots at that position
        if grid[y][x] == 0:
            grid[y][x] = 1
        else:
            grid[y][x] += 1
    
    return grid

# Function to move robots based on their velocity over a given time (seconds)
def moveRobots(robotList, seconds):
    newList = []
    for r in robotList:
        # Extract current position and velocity
        x, y = r[0][0], r[0][1]
        vx, vy = r[1][0], r[1][1]
        
        # Update position based on velocity and time
        x += vx * seconds
        y += vy * seconds
        
        # Append updated position and velocity to the new list
        newList.append(((x, y), (vx, vy)))

    return newList

# Function to create a quadrant of the grid based on the middle point (center)
def createQuadrant(grid, middleX, middleY, position):
    quadrant = []
    # Determine the range for the specific quadrant based on the position value
    match position:
        case 0:  # Top-left quadrant
            rangeY = range(middleY)
            rangeX = range(middleX)
        case 1:  # Top-right quadrant
            rangeY = range(middleY)
            rangeX = range(middleX + 1, len(grid[0]))
        case 2:  # Bottom-left quadrant
            rangeY = range(middleY + 1, len(grid))
            rangeX = range(middleX)
        case 3:  # Bottom-right quadrant
            rangeY = range(middleY + 1, len(grid))
            rangeX = range(middleX + 1, len(grid[0]))
    
    # Build the quadrant by selecting the corresponding grid elements
    for i in rangeY:
        row = []
        for j in rangeX:
            row.append(grid[i][j])
        quadrant.append(row)
    
    return quadrant

# Function to calculate the safety factor by dividing the grid into four quadrants
def calculateSafetyFactor(grid, width, height):
    # Calculate the middle points of the grid
    middleX = width // 2
    middleY = height // 2

    # Initialize empty lists for the quadrants
    q1, q2, q3, q4 = [], [], [], []
    quadrantList = [q1, q2, q3, q4]
    
    # Create quadrants based on the grid
    for i in range(len(quadrantList)):
        quadrantList[i] = createQuadrant(grid, middleX, middleY, i)

    return quadrantList

# Function to read the file and initialize robot positions and velocities
def readFile(time):
    # Open the file containing robot data
    with open("2024/D14.txt", "r") as file:
        robots = []
        for row in file:
            # Split the row into position and velocity strings
            position, velocity = row.strip("\n").split(" ")

            # Extract position (X, Y) and velocity (VX, VY) values
            pX, pY = map(int, position.split("=")[1].split(","))
            vX, vY = map(int, velocity.split("=")[1].split(","))
            
            # Append the robot data as a tuple (position, velocity)
            robots.append(([[pX, pY], (vX, vY)]))
        
    # Define the grid dimensions
    WIDTH = 101
    HEIGHT = 103

    # Move robots and create the grid
    robots = moveRobots(robots, time)
    grid = createGrid(robots, WIDTH, HEIGHT)
    return grid, WIDTH, HEIGHT

# Measure execution time
import time

start_time = time.time()  # Start the timer

# Read the file and initialize the grid
grid, WIDTH, HEIGHT = readFile(100)

# Calculate quadrants and safety factor
quadrants = calculateSafetyFactor(grid, WIDTH, HEIGHT)

safetyFactor = 1
# Calculate the safety factor by multiplying the sum of each quadrant
for q in quadrants:
    # Sum the values in each quadrant and multiply to compute the safety factor
    sumValues = sum(sum(n) for n in q)
    safetyFactor *= sumValues

print("Safety factor:", safetyFactor)

# Start a loop to move robots and check for an Easter Egg
run = True
# Initialize the time variable
t = 6000

while run:
    # Update the grid with new positions
    grid, WIDTH, HEIGHT = readFile(t)
    quadrants = calculateSafetyFactor(grid, WIDTH, HEIGHT)

    # Print the grid and check for an Easter Egg (a specific pattern)
    for i in range(HEIGHT):
        row = ""
        for j in range(WIDTH):
            # Represent empty cells with a space and occupied cells with a dash
            if grid[i][j] == 0:
                row += " "
            else:
                row += "-"
        
        # Check for the Easter Egg pattern in the row
        if "-------------------------------" in row:
            print("Easter Egg:", t)
            run = False
            break
        if not run:  # Ensure the loop exits correctly
            break
    if run:
        t += 1  # Increment the time variable if no Easter Egg is found

end_time = time.time()  # End the timer
print(f"{end_time - start_time:.6f} seconds")  # Print the execution time