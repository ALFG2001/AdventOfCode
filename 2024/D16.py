from heapq import heappop, heappush

# Open and read the maze from the input file
with open("2024/D16.txt") as f:
    lines = [l.strip() for l in f]

# Determine maze dimensions and initialize variables
dimx, dimy = len(lines[0]), len(lines)  # Width (dimx) and height (dimy) of the maze
maze = list("".join(lines))  # Flatten the 2D maze into a 1D string representation
start, end = maze.index("S"), maze.index("E")  # Find the positions of the start ('S') and end ('E')
dirs = [-dimx, 1, dimx, -1]  # Directions to move in the maze: up, right, down, left (relative to index)

# A dictionary to track the best score (shortest path) for each position and direction
visited = dict()

# A priority queue for A* algorithm (heap queue), to store positions to explore
q = list()

# Highscore is initially set to infinity; it will track the shortest path found
highscore = float('inf')

# List to store the paths that lead to the goal
paths = list()

# Initialize the priority queue with the start position (score, position, direction, path)
heappush(q, (0, start, 1, ""))

# A* search loop to find the shortest path and all possible paths
while q:
    score, pos, d, path = heappop(q)  # Pop the position with the lowest score from the queue
    
    # If the current score exceeds the best score found, stop the search
    if score > highscore:
        break
    
    # Skip if we've already visited this position and direction with a lower or equal score
    if (pos, d) in visited and visited[(pos, d)] < score:
        continue
    
    # Mark the current position and direction as visited with the best score
    visited[(pos, d)] = score
    
    # If the end is reached, update the highscore and store the path
    if pos == end:
        highscore = score
        paths.append(path)
    
    # Explore the next position in the current direction, if it's not a wall ('#')
    if maze[pos + dirs[d]] != "#":
        heappush(q, (score + 1, pos + dirs[d], d, path + "F"))  # Move forward (F)
    
    # Explore the next direction by rotating right (clockwise)
    heappush(q, (score + 1000, pos, (d + 1) % 4, path + "R"))  # Turn right (R)
    
    # Explore the next direction by rotating left (counterclockwise)
    heappush(q, (score + 1000, pos, (d - 1) % 4, path + "L"))  # Turn left (L)

# Set to store unique positions that are part of the optimal path or the shortest path
tiles = set()
tiles.add(start)  # Add the start position to the set

# For each valid path found, calculate the positions visited and add them to the set
for p in paths:
    t, d = start, 1  # Start at the starting position, facing right (direction 1)
    
    # Traverse the path and update positions based on the directions
    for c in p:
        if c == "L":  # Turn left
            d = (d - 1) % 4
        elif c == "R":  # Turn right
            d = (d + 1) % 4
        elif c == "F":  # Move forward in the current direction
            t += dirs[d]
            tiles.add(t)  # Add the new position to the set of visited tiles

# Output the results: shortest path length and number of unique tiles visited
print(f"Shortest path: {highscore}")
print(f"Optimal viewing positions: {len(tiles)}")
