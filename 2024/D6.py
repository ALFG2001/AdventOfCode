def guard():
    def move(symbol, posX, posY, grid, visited_cells: set):
        match symbol:
            case "^":
                movement = [0, -1]
                right = ">"
            case "v":
                movement = [0, +1]
                right = "<"
            case ">":
                movement = [+1, 0]
                right = "v"
            case "<":
                movement = [-1, 0]
                right = "^"

        newY = posY + movement[1]
        newX = posX + movement[0]

        if newY < 0 or newY >= len(grid) or newX < 0 or newX >= len(grid[0]):
            return True, newX, newY, symbol

        target_cell = grid[newY][newX]

        if target_cell == "#":
            return move(right, posX, posY, grid, visited_cells)

        grid[newY][newX] = symbol
        visited_cells.add((newX, newY))
        historical_cells.append((newX, newY, symbol))
        return False, newX, newY, symbol

    def moveLoop(symbol, posX, posY, grid, history: set):
        match symbol:
            case "^":
                movement = [0, -1]
                right = ">"
            case "v":
                movement = [0, +1]
                right = "<"
            case ">":
                movement = [+1, 0]
                right = "v"
            case "<":
                movement = [-1, 0]
                right = "^"

        newY = posY + movement[1]
        newX = posX + movement[0]

        if newY < 0 or newY >= len(grid) or newX < 0 or newX >= len(grid[0]):
            return True, newX, newY, symbol, False

        target_cell = grid[newY][newX]

        if target_cell == "#":
            return moveLoop(right, posX, posY, grid, history)
        
        grid[posY][posX] = "X"
        grid[newY][newX] = symbol 

        current_state = (newX, newY, symbol)
        if current_state in history:
            return True, newX, newY, symbol, True

        history.add(current_state)

        return False, newX, newY, symbol, False

    grid = []
    grid_copy = []
    obstacles = []
    unique_cells = set()
    historical_cells = []

    with open("2024/D6.txt", "r") as file:
        y = 0
        for line in file:
            grid.append([c for c in line.strip("\n")])
            grid_copy.append([c if c in '.#' else '.' for c in line.strip("\n")])
            try:
                x = line.index("^")
                start = (x, y)
            except ValueError:
                y += 1
            
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                obstacles.append((j, i))

    exit_flag = False
    x, y = start[0], start[1]
    unique_cells.add((x, y))
    symbol = "^"
    while not exit_flag:
        exit_flag, x, y, symbol = move(symbol, x, y, grid, unique_cells)

    print("Unique Cells:", len(unique_cells))

    loop_positions = []

    map_index = 0
    for x, y in unique_cells:
        oX, oY = x, y
        map_copy = [row[:] for row in grid_copy]

        map_copy[oY][oX] = "#"

        visited_states = set()
        exit_loop = False

        sx, sy = start
        p = "^"
        
        while not exit_loop:
            
            exit_loop, sx, sy, p, loop_flag = moveLoop(
                p, sx, sy, map_copy, visited_states
            )    

        if loop_flag:
            loop_positions.append((oX, oY))

        map_index += 1

    print("Number of Obstacles:", len(loop_positions))

import time

start_time = time.time()
guard()
end_time = time.time()
print(f"{end_time - start_time:.6f} seconds")
