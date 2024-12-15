def parse_input(path):
    with open(path, "r") as file:
        grid = []  # To store the grid representation
        rules = []  # To store movement rules
        append_rules = False  # Flag to start appending rules
        for row_index, row in enumerate(file):
            row = row.strip("\n")  # Split row by spaces
            if not row:
                append_rules = True  # Start appending rules after an empty row

            if append_rules:
                for symbol in row:
                    rules.append({
                        "^": (-1, 0),  # Move up
                        "v": (1, 0),   # Move down
                        ">": (0, 1),   # Move right
                        "<": (0, -1)   # Move left
                    }[symbol])
            else:
                for column_index, cell in enumerate(row):
                    if cell == "@":
                        start_position = (row_index, column_index)  # Starting position of the robot
                grid.append(list(row))  # Add the current row to the grid

        return grid, rules, start_position

def move(grid, direction, robot_position, symbol):
    new_y = robot_position[0] + direction[0]  # New row position
    new_x = robot_position[1] + direction[1]  # New column position

    # Check if the robot hits a wall
    if grid[new_y][new_x] == "#":
        new_y, new_x = robot_position  # Stay in the same position if hit a wall

    # If the robot moves onto a box
    elif grid[new_y][new_x] == "O":
        box_y, box_x = move(grid, direction, (new_y, new_x), "O")  # Move the box
        if new_y == box_y and new_x == box_x:
            new_y, new_x = robot_position  # Prevent the robot from being stuck

    # If the robot moves onto a pair of boxes
    elif grid[new_y][new_x] == "[":
        if direction[0] == 0:
            box_y, box_x = move(grid, direction, (new_y, new_x), "[")
            if new_y == box_y and new_x == box_x:
                new_y, new_x = robot_position  # Prevent robot from getting stuck
        else:
            if can_move_vertical(grid, direction, (new_y, new_x), "["):
                move(grid, direction, (new_y, new_x), "[")
                move(grid, direction, (new_y, new_x + 1), "]")
            else:
                new_y, new_x = robot_position

    # If the robot moves onto a pair of boxes (in opposite direction)
    elif grid[new_y][new_x] == "]":
        if direction[0] == 0:
            box_y, box_x = move(grid, direction, (new_y, new_x), "]")
            if new_y == box_y and new_x == box_x:
                new_y, new_x = robot_position
        else:
            if can_move_vertical(grid, direction, (new_y, new_x), "]"):
                move(grid, direction, (new_y, new_x), "]")
                move(grid, direction, (new_y, new_x - 1), "[")
            else:
                new_y, new_x = robot_position

    grid[robot_position[0]][robot_position[1]] = "."  # Clear the old robot position
    grid[new_y][new_x] = symbol  # Place robot at the new position

    new_position = (new_y, new_x)  # Update robot's position
    return new_position

def can_move_vertical(grid, direction, robot_position, symbol):
    new_y = robot_position[0] + direction[0]  # Check vertical movement (row)
    new_x = robot_position[1]  # Keep the column fixed

    # Determine the pair's column for vertical movement (left or right box)
    match symbol:
        case "[":
            pair_x = new_x + 1  # Right box for the pair
        case "]":
            pair_x = new_x - 1  # Left box for the pair

    # If there's a wall at either target position, we can't move
    if grid[new_y][new_x] == "#" or grid[new_y][pair_x] == "#":
        return False
    else:
        # If both target positions are boxes, check if we can move both vertically
        if grid[new_y][new_x] in ("[", "]") and grid[new_y][pair_x] in ("[", "]"):
            return can_move_vertical(grid, direction, (new_y, new_x), grid[new_y][new_x]) and can_move_vertical(grid, direction, (new_y, pair_x), grid[new_y][pair_x])
        elif grid[new_y][new_x] in ("[", "]"):
            # If only the first position is a box, recursively check vertical movement for both
            if grid[new_y][new_x] == "[":
                return can_move_vertical(grid, direction, (new_y, new_x), grid[new_y][new_x]) and can_move_vertical(grid, direction, (new_y, new_x + 1), grid[new_y][new_x + 1])
            else:
                return can_move_vertical(grid, direction, (new_y, new_x), grid[new_y][new_x]) and can_move_vertical(grid, direction, (new_y, new_x - 1), grid[new_y][new_x - 1])
        elif grid[new_y][pair_x] in ("[", "]"):
            # If only the second position is a box, recursively check vertical movement for both
            if grid[new_y][pair_x] == "[":
                return can_move_vertical(grid, direction, (new_y, pair_x), grid[new_y][pair_x]) and can_move_vertical(grid, direction, (new_y, pair_x + 1), grid[new_y][pair_x + 1])
            else:
                return can_move_vertical(grid, direction, (new_y, pair_x), grid[new_y][pair_x]) and can_move_vertical(grid, direction, (new_y, pair_x - 1), grid[new_y][pair_x - 1])
        
    return True  # If no issues found, return True

def make_new_grid(grid):
    new_grid = []  # To store the newly generated grid
    for row in grid:
        new_row = []  # To store the modified row
        for symbol in row:
            match symbol:
                case "#":
                    new_row.extend(["#","#"])  # Walls become double walls
                case "O":
                    new_row.extend(["[","]"])  # Boxes become a large box
                case ".":
                    new_row.extend([".","."])  # Empty spaces remain as empty spaces
                case "@":
                    new_row.extend(["@","."])  # Start position is followed by an empty space
        new_grid.append(new_row)

    return new_grid

def calculate_gps(grid, symbol, rules, position):
    for rule in rules:
        position = move(grid, rule, position, "@")  # Move robot according to the rules

    gps = 0  # Initialize GPS calculation
    for row_index, row in enumerate(grid):
        for column_index, cell in enumerate(row):
            if cell == symbol:
                gps += 100 * row_index + column_index  # Calculate GPS based on position of the symbol
    return gps

def main():
    grid, rules, start_position = parse_input("2024/D15.txt")  # Parse input file
    new_grid = make_new_grid(grid)  # Create new grid with modified structure
    new_position = (start_position[0], start_position[1] * 2)  # Adjust starting position for new grid

    gps1 = calculate_gps(grid, "O", rules, start_position)  # Calculate GPS for the original grid
    print("GPS for the first grid:", gps1)

    gps2 = calculate_gps(new_grid, "[", rules, new_position)  # Calculate GPS for the new grid
    print("GPS for the second grid:", gps2)

# Measure execution time
import time

start_time = time.time()  # Start the timer
main()  # Call the function
end_time = time.time()  # End the timer
print(f"Execution time: {end_time - start_time:.6f} seconds")  # Print the execution time
