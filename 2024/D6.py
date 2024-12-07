def guard():
    # Function to handle movement of the guard
    def move(symbol, posX, posY, grid, visited_cells: set):
        # Match the symbol (direction) and define corresponding movement
        match symbol:
            case "^":  # Moving up
                movement = [0, -1]
                right = ">"
            case "v":  # Moving down
                movement = [0, +1]
                right = "<"
            case ">":  # Moving right
                movement = [+1, 0]
                right = "v"
            case "<":  # Moving left
                movement = [-1, 0]
                right = "^"

        # Calculate the new position based on movement
        newY = posY + movement[1]
        newX = posX + movement[0]

        # Check if the new position is out of bounds
        if newY < 0 or newY >= len(grid) or newX < 0 or newX >= len(grid[0]):
            return True, newX, newY, symbol  # Return exit flag, new coordinates, and symbol

        target_cell = grid[newY][newX]  # Get the content of the new cell

        # If the new cell is an obstacle, change direction
        if target_cell == "#":
            return move(right, posX, posY, grid, visited_cells)

        # If the target cell is not an obstacle, add the new position to visited cells
        visited_cells.add((newX, newY))
        historical_cells.append((newX, newY, symbol))  # Track the historical movement

        return False, newX, newY, symbol  # Return that we didn't exit and updated position

    # Function to handle loop detection in the guard's movement
    def moveLoop(symbol, posX, posY, grid, history: set):
        match symbol:
            case "^":  # Moving up
                movement = [0, -1]
                right = ">"
            case "v":  # Moving down
                movement = [0, +1]
                right = "<"
            case ">":  # Moving right
                movement = [+1, 0]
                right = "v"
            case "<":  # Moving left
                movement = [-1, 0]
                right = "^"

        # Calculate the new position based on movement
        newY = posY + movement[1]
        newX = posX + movement[0]

        # Check if the new position is out of bounds
        if newY < 0 or newY >= len(grid) or newX < 0 or newX >= len(grid[0]):
            return True, newX, newY, symbol, False  # Exit condition, no loop

        target_cell = grid[newY][newX]  # Get the content of the new cell

        # If the new cell is an obstacle, change direction
        if target_cell == "#":
            return moveLoop(right, posX, posY, grid, history)

        # Check if this position with the same symbol has been visited (loop detection)
        current_state = (newX, newY, symbol)
        if current_state in history:
            return True, newX, newY, symbol, True  # Loop detected

        # Add the current state (position and symbol) to the visited history
        history.add(current_state)

        return False, newX, newY, symbol, False  # Continue moving

    # Initializing variables
    grid = []  # The grid where the guard will move
    grid_copy = []  # A copy of the grid for later manipulation
    obstacles = []  # List of obstacles in the grid
    unique_cells = set()  # Set of cells visited by the guard
    historical_cells = []  # List to track the guard's movement history

    # Read the grid from the input file
    with open("2024/D6.txt", "r") as file:
        y = 0
        for line in file:
            grid.append([c for c in line.strip("\n")])  # Add the grid row
            grid_copy.append([c if c in '.#' else '.' for c in line.strip("\n")])  # Copy grid, change symbols
            try:
                x = line.index("^")  # Try to find the starting position
                start = (x, y)  # Set the starting position
            except ValueError:  # If starting symbol is not found, continue to next row
                y += 1
            
    # Identify obstacles in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                obstacles.append((j, i))  # Record the obstacle positions

    # Initialize variables for the guard's movement
    exit_flag = False  # Flag for detecting if the guard should stop
    x, y = start[0], start[1]  # Starting coordinates
    unique_cells.add((x, y))  # Add starting point to visited cells
    symbol = "^"  # Starting direction (up)

    # Start the guard's movement loop
    while not exit_flag:
        exit_flag, x, y, symbol = move(symbol, x, y, grid, unique_cells)

    print("Unique Cells:", len(unique_cells))  # Print the number of unique cells visited

    loop_positions = []  # List to track positions where loops are detected

    map_index = 0
    # Check for loops in the movement by visiting each unique cell and testing for loops
    for x, y in unique_cells:
        oX, oY = x, y
        map_copy = [row[:] for row in grid_copy]  # Copy the grid again

        map_copy[oY][oX] = "#"  # Mark the current cell as an obstacle to test if it causes a loop

        visited_states = set()  # Set to track visited states during loop detection
        exit_loop = False  # Flag to stop the loop

        sx, sy = start  # Reset starting position for the loop detection
        p = "^"  # Reset starting direction
        
        # Loop to check for loops while moving
        while not exit_loop:
            exit_loop, sx, sy, p, loop_flag = moveLoop(p, sx, sy, map_copy, visited_states)

        # If a loop was detected, add the position to loop_positions
        if loop_flag:
            loop_positions.append((oX, oY))

        map_index += 1

    # Print the number of positions where loops were detected
    print("Number of Obstacles:", len(loop_positions))

# Measure the execution time
import time

start_time = time.time()  # Start time for measuring performance
guard()  # Call the main function
end_time = time.time()  # End time after execution
print(f"{end_time - start_time:.6f} seconds")  # Print the execution time
