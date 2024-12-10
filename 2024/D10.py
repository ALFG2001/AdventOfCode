def rateMap():    
    # Function to create the dictionary that maps positions in the grid to their neighbors
    def createDictionary(startDictionary, grid):
        # Iterate over each key in the starting dictionary
        for key in startDictionary:
            startX = key[1]  # Column (X) of the key
            startY = key[0]  # Row (Y) of the key
            startValue = grid[startY][startX]  # Value at the starting position in the grid
            
            # Ensure the key has an internal dictionary
            if key not in startDictionary:
                startDictionary[key] = {}
            
            # Check neighbors (above, below, left, right) and add to dictionary if the value is `startValue + 1`
            if startY > 0 and grid[startY - 1][startX] == startValue + 1:
                startDictionary[key][(startY - 1, startX)] = {}
            
            if startY < len(grid) - 1 and grid[startY + 1][startX] == startValue + 1:
                startDictionary[key][(startY + 1, startX)] = {}
            
            if startX > 0 and grid[startY][startX - 1] == startValue + 1:
                startDictionary[key][(startY, startX - 1)] = {}
            
            if startX < len(grid[0]) - 1 and grid[startY][startX + 1] == startValue + 1:
                startDictionary[key][(startY, startX + 1)] = {}
        
        return startDictionary

    # Recursive function to create the dictionary up to a maximum level
    def createRecursiveDictionary(startDictionary, grid, maxLevel, currentLevel=0):
        # Base case: stop when the maximum level is reached
        if currentLevel >= maxLevel:
            return startDictionary
        
        # Update the dictionary for the current level
        updatedDictionary = createDictionary(startDictionary, grid)
        
        # For each key in the dictionary, recursively call the function
        for key in updatedDictionary:
            updatedDictionary[key] = createRecursiveDictionary(
                updatedDictionary[key],
                grid,
                maxLevel,
                currentLevel + 1
            )
        
        return updatedDictionary

    # Function to calculate the paths that reach the maximum value in the grid
    def calculatePaths(dictionary, grid, maxValue, currentPath=None):
        if currentPath is None:
            currentPath = []
        
        paths = []
        for key, subDictionary in dictionary.items():
            newPath = currentPath + [key]  # Add the current key to the path
            
            # Check if we're on a cell with the maximum value
            if grid[key[0]][key[1]] == maxValue:
                paths.append(newPath)
            else:  # Continue exploring the sub-dictionary
                paths += calculatePaths(subDictionary, grid, maxValue, newPath)
        
        return paths

    # Initialize the starting dictionary
    startDictionary = {}

    # Read the grid and initialize the startDictionary
    with open("2024/D10.txt", "r") as file:
        grid = []
        for i, row in enumerate(file):
            rowList = []
            for j, num in enumerate(row.strip("\n")):
                rowList.append(int(num))
                if int(num) == 0:
                    startDictionary[(i, j)] = {}
            grid.append(rowList)

    # Determine the maximum number in the grid
    maxNumber = max(max(row) for row in grid)

    # Create the full dictionary up to the maximum level
    startDictionary = createRecursiveDictionary(startDictionary, grid, maxLevel=maxNumber)

    # Find the maximum value in the grid
    maxValue = max(max(row) for row in grid)

    # Calculate the unique paths from the dictionary
    uniquePaths = []
    for initialKey in startDictionary:
        uniquePaths += calculatePaths({initialKey: startDictionary[initialKey]}, grid, maxValue)

    # Print the paths
    print("Unique paths that reach a cell with the maximum value:")
    startEndUnique = set()
    for path in uniquePaths:
        startEndUnique.add((path[0], path[-1]))

    # Total number of paths
    print("Total scores:", len(startEndUnique))
    print("Total ratings:", len(uniquePaths))


# Measure execution time
import time

start_time = time.time()  # Start the timer
rateMap()  # Call the function
end_time = time.time()  # End the timer
print(f"{end_time - start_time:.6f} seconds")  # Print the execution time
