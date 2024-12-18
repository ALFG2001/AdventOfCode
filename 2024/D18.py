import time

def find_neighbors(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def find_path(grid, start_coord, end_coord):
    # Get grid dimensions
    rows, cols = len(grid), len(grid[0])

    def is_valid(coord):
        x, y = coord
        # Check if the coordinates are within bounds and not an obstacle
        return 0 <= x < cols and 0 <= y < rows and grid[y][x] != "#"

    # Dictionary to track visited nodes and distances
    visited = {start_coord: 0}
    distance = 1
    current_layer = [start_coord]  # Start from the starting coordinate

    # Perform BFS
    while current_layer:
        next_layer = []
        for node in current_layer:
            for neighbor in find_neighbors(*node):
                if neighbor not in visited and is_valid(neighbor):
                    visited[neighbor] = distance
                    next_layer.append(neighbor)
        current_layer = next_layer
        distance += 1

    # If the end point is not reachable, return False
    if end_coord not in visited:
        return False

    # Reconstruct the path
    path = []
    current = end_coord
    while current != start_coord:
        path.append(current)
        current = min(
            [neighbor for neighbor in find_neighbors(*current) if neighbor in visited],
            key=lambda x: visited[x]
        )
    path.append(start_coord)
    return path[::-1]  # Return the path from start to end

# Start timing the execution
start_time = time.time()

# Read obstacles from file
obstacles = []
threshold = 1024
with open("2024/D18.txt", "r") as file:
    for line_number, line in enumerate(file):
        obstacles.append(tuple(map(int, line.strip("\n").split(","))))

grid_size = 71

# Create the grid
grid = [["#" if (col, row) in obstacles[:threshold] else "." for col in range(grid_size)] for row in range(grid_size)]
remaining_obstacles = obstacles[threshold:]

start = (0, 0)
end = (70, 70)  # Ensure the endpoint is within the grid bounds

# Compute the initial path
path = find_path(grid, start, end)
if path:
    print("Path length:", len(path) - 1)
else:
    print("No initial path found.")

# Add remaining obstacles and check for path break
obstacle_index = len(remaining_obstacles)-1
grid = [["#" if (col, row) in obstacles else "." for col in range(grid_size)] for row in range(grid_size)]
while True:
    x, y = remaining_obstacles[obstacle_index]
    grid[y][x] = "."  # Add the next obstacle
    if find_path(grid, start, end):
        print(f"Obstacle breaking path: {x},{y}")
        break
    else:
        obstacle_index -= 1

# Print execution time
end_time = time.time()
print(f"Execution time: {end_time - start_time:.2f} seconds")
