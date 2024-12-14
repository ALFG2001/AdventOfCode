# Open the file containing robot data
with open("2024/D14.txt", "r") as file:
    robots = []
    for row in file:
        position, velocity = row.strip("\n").split(" ")

        # Extract position (X, Y) and velocity (VX, VY)
        pX, pY = map(int, position.split("=")[1].split(","))
        vX, vY = map(int, velocity.split("=")[1].split(","))
        
        # Append the robot data as a tuple (position, velocity)
        robots.append(([[pX, pY], (vX, vY)]))

# Function to create the grid (2D array) with specified width and height
def createGrid(width, height):
    global robots
    grid = []
    
    # Initialize a grid filled with zeros
    for y in range(height):
        row = []
        for x in range(width):
            row.append(0)
        grid.append(row)

    # Place robots on the grid based on their positions
    for robot in robots:
        x, y = robot[0][0] % width, robot[0][1] % height
        if grid[y][x] == 0:
            grid[y][x] = 1
        else:
            grid[y][x] += 1
    
    return grid

# Function to move robots based on their velocity over a given time (seconds)
def moveRobots(robotList, seconds):
    newList = []
    for r in robotList:
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
        case 0:
            rangeY = range(middleY)
            rangeX = range(middleX)
        case 1:
            rangeY = range(middleY)
            rangeX = range(middleX + 1, len(grid[0]))
        case 2:
            rangeY = range(middleY + 1, len(grid))
            rangeX = range(middleX)
        case 3:
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
    middleX = width // 2
    middleY = height // 2

    q1, q2, q3, q4 = [], [], [], []
    quadrantList = [q1, q2, q3, q4]
    
    # Create quadrants based on the grid
    for i in range(len(quadrantList)):
        quadrantList[i] = createQuadrant(grid, middleX, middleY, i)

    return quadrantList

# Measure execution time
import time

start_time = time.time()  # Start the timer
    
WIDTH = 101
HEIGHT = 103
TIME = 100

# Move robots and create the grid
robots = moveRobots(robots, TIME)
grid = createGrid(WIDTH, HEIGHT)

# Calculate quadrants and safety factor
quadrants = calculateSafetyFactor(grid, WIDTH, HEIGHT)

safetyFactor = 1
# Calculate the safety factor by multiplying the sum of each quadrant
for q in quadrants:
    sumValues = sum(sum(n) for n in q)
    safetyFactor *= sumValues

print("Safety factor:", safetyFactor)



TIME = 6000

run = True
# Start a loop to move robots and check for an Easter Egg
while run:

    # Re-reading the file to initialize robots again
    with open("2024/D14.txt", "r") as file:
        robots = []
        for row in file:
            position, velocity = row.strip("\n").split(" ")

            pX, pY = map(int, position.split("=")[1].split(","))
            vX, vY = map(int, velocity.split("=")[1].split(","))
            robots.append(([[pX, pY], (vX, vY)]))

    robots = moveRobots(robots, TIME)
    grid = createGrid(WIDTH, HEIGHT)
    quadrants = calculateSafetyFactor(grid, WIDTH, HEIGHT)


    # Print the grid and check for an Easter Egg (a specific pattern)
    for i in range(HEIGHT):
        row = ""
        for j in range(WIDTH):
            if grid[i][j] == 0:
                row += " "
            else:
                row += "-"
        
        # Check for the Easter Egg
        if "-------------------------------" in row:
            print("Easter Egg:", TIME)
            run = False
            break
        if not run:
            break
    if run:
        TIME += 1


end_time = time.time()  # End the timer
print(f"{end_time - start_time:.6f} seconds")  # Print the execution time
