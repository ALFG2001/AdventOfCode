import os
import time
import sys

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
                row = list(row)
                for column_index, cell in enumerate(row):
                    if cell == "@":
                        start_position = (row_index, column_index)  # Starting position of the robot
                    if cell == ".":
                        row[column_index] = " "
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

    grid[robot_position[0]][robot_position[1]] = " "  # Clear the old robot position
    grid[new_y][new_x] = symbol  # Place robot at the new position

    new_position = (new_y, new_x)  # Update robot's position
    return new_position

def can_move_vertical(grid, direction, robot_position, symbol):
    # Calculate new positions
    new_y = robot_position[0] + direction[0]  # Vertical movement (row)
    new_x = robot_position[1]  # Keep the column fixed

    # Determine the pair's column based on the symbol
    if symbol == "[":
        pair_x = new_x + 1  # Right box for the pair
    elif symbol == "]":
        pair_x = new_x - 1  # Left box for the pair

    # Check if the new positions are blocked by walls
    if grid[new_y][new_x] == "#" or  grid[new_y][pair_x] == "#":
        return False

    # Check if both positions are boxes
    if grid[new_y][new_x] in ("[", "]") and grid[new_y][pair_x] in ("[", "]"):
        # Recursively check vertical movement for both boxes
        return (
            can_move_vertical(grid, direction, (new_y, new_x), grid[new_y][new_x]) and
            can_move_vertical(grid, direction, (new_y, pair_x), grid[new_y][pair_x])
        )

    # Handle case where only one position is a box
    if grid[new_y][new_x] in ("[", "]"):
        return can_move_vertical_for_box(grid, direction, new_y, new_x)
    
    if pair_x is not None and grid[new_y][pair_x] in ("[", "]"):
        return can_move_vertical_for_box(grid, direction, new_y, pair_x)

    return True  # No issues found, movement is allowed


def can_move_vertical_for_box(grid, direction, new_y, box_x):
    # Recursive check for vertical movement for a box and its pair
    if grid[new_y][box_x] == "[":
        return (
            can_move_vertical(grid, direction, (new_y, box_x), grid[new_y][box_x]) and
            can_move_vertical(grid, direction, (new_y, box_x + 1), grid[new_y][box_x + 1])
        )
    elif grid[new_y][box_x] == "]":
        return (
            can_move_vertical(grid, direction, (new_y, box_x), grid[new_y][box_x]) and
            can_move_vertical(grid, direction, (new_y, box_x - 1), grid[new_y][box_x - 1])
        )
    else:
        # If the box is neither "[" nor "]", return True (no box movement needed)
        return True


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
                case " ":
                    new_row.extend([" "," "])  # Empty spaces remain as empty spaces
                case "@":
                    new_row.extend(["@"," "])  # Start position is followed by an empty space
        new_grid.append(new_row)

    return new_grid

def calculate_gps(grid, symbol):
    gps = 0  # Initialize GPS calculation
    for row_index, row in enumerate(grid):
        for column_index, cell in enumerate(row):
            if cell == symbol:
                gps += 100 * row_index + column_index  # Calculate GPS based on position of the symbol
    return gps

def print_grids_side_by_side(grid1, grid2):
    """Function to print two grids side by side with colored symbols."""
    sys.stdout.write("\033[H")  # Move cursor to the top-left corner
    sys.stdout.flush()

    for row1, row2 in zip(grid1, grid2):
        row_str1 = ""
        row_str2 = ""
        
        # For grid1
        for symbol in row1:
            if symbol == "@":
                row_str1 += "🤖"  # Robot
            elif symbol == "O":
                row_str1 += "📦"  # Boxes
            elif symbol == "#": 
                row_str1 += "🧱"  # Wall
            else:
                row_str1 += "⠀⠀"  # Empty space
                
        # For grid2 (similar formatting for the new grid)
        for symbol in row2:
            if symbol == "@":
                row_str2 += "🤖"  # Robot
            elif symbol == "[": 
                row_str2 += "⏪"  # Left side of the box
            elif symbol == "]": 
                row_str2 += "⏩"  # Right side of the box
            elif symbol == "#": 
                row_str2 += "🧱"  # Wall
            else:
                row_str2 += "⠀⠀"  # Empty space
        
        print(" "*20 + row_str1 + " "*20 + row_str2)  # Add space between the grids


def animate_grid_change(grid1, grid2, start_position1, start_position2, rules):
    """Animate the grid change step-by-step without screen flashing for both grids."""
    position1 = start_position1
    position2 = start_position2

    # Print both grids side by side initially
    print_grids_side_by_side(grid1, grid2)
    time.sleep(2)  # Pause before starting animation

    # Animate movement for both grids
    for rule in rules:
        # Move robot in grid1
        position1 = move(grid1, rule, position1, "@")
        # Move robot in grid2 (this assumes the movement rules are applied similarly)
        position2 = move(grid2, rule, position2, "@")

        # Print both grids side by side after the move
        print_grids_side_by_side(grid1, grid2)
        
def main():
    grid, rules, start_position1 = parse_input("2024/D15.txt")  # Parse input file
    new_grid = make_new_grid(grid)  # Create new grid with modified structure
    start_position2 = (start_position1[0], start_position1[1] * 2)  # Adjust starting position for new grid
    # Animate the grid change for both grids
    animate_grid_change(grid, new_grid, start_position1, start_position2, rules)  # Animate both grid

    gps1 = calculate_gps(grid, "O")  # Calculate GPS for the original grid
    print("GPS for the first grid:", gps1)

    gps2 = calculate_gps(new_grid, "[")  # Calculate GPS for the new grid
    print("GPS for the second grid:", gps2)


# Measure execution time
start_time = time.time()  # Start the timer
main()  # Call the function
end_time = time.time()  # End the timer
print(f"Execution time: {end_time - start_time:.6f} seconds")  # Print the execution time
