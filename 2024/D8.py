# Dictionary to store antenna positions
antennaPositions = {}
maxY = 0
maxX = 0

# Read the file and parse antenna positions
with open("2024/D8.txt", "r") as file:
    for i, row in enumerate(file):
        for j, antenna in enumerate(row.strip("\n")):
            if antenna != ".":  # Skip empty positions
                if antenna not in antennaPositions:
                    antennaPositions[antenna] = [(i, j)]
                else:
                    antennaPositions[antenna].append((i, j))

    maxY = i  # Maximum Y coordinate
    maxX = j  # Maximum X coordinate

# Function to find anti-nodes aligned with the given positions
def findAntiNodes(positionList, maxX, maxY):
    antiNodeList = []

    for i, pos in enumerate(positionList):
        otherPositions = positionList[:i] + positionList[i + 1:]  # All other nodes
        for node in otherPositions:
            # Calculate horizontal and vertical distances
            distY = node[0] - pos[0]
            distX = node[1] - pos[1]

            # Generate aligned anti-nodes (on the same diagonal, horizontal, or vertical line)
            anti1 = (pos[0] - distY, pos[1] - distX)  # Opposite aligned node
            anti2 = (node[0] + distY, node[1] + distX)  # Opposite node on the other side

            # Add only valid anti-nodes (within grid boundaries)
            for anti in [anti1, anti2]:
                if 0 <= anti[0] <= maxY and 0 <= anti[1] <= maxX:
                    antiNodeList.append(anti)

    return antiNodeList

# Function to find extended anti-nodes aligned with the given positions
def findExtendedAntiNodes(positionList, maxX, maxY):
    extendedAntiNodes = set()

    for i, pos in enumerate(positionList):
        otherPositions = positionList[:i] + positionList[i + 1:]  # All other nodes
        for node in otherPositions:
            # Calculate horizontal and vertical distances
            distY = node[0] - pos[0]
            distX = node[1] - pos[1]

            direction = (distY, distX)  # Direction of alignment

            # Extend in the negative direction
            current = pos
            while True:
                newPoint = (current[0] - direction[0], current[1] - direction[1])
                if 0 <= newPoint[0] <= maxY and 0 <= newPoint[1] <= maxX:
                    extendedAntiNodes.add(newPoint)
                    current = newPoint
                else:
                    break

            # Extend in the positive direction
            current = node
            while True:
                newPoint = (current[0] + direction[0], current[1] + direction[1])
                if 0 <= newPoint[0] <= maxY and 0 <= newPoint[1] <= maxX:
                    extendedAntiNodes.add(newPoint)
                    current = newPoint
                else:
                    break

    return extendedAntiNodes

# Function to count anti-nodes in the grid
def countAntiNodes(rows, antiNodeList, antennaPositions, extended=False):
    counter = 0
    antiNodeSet = set(antiNodeList)

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if (i, j) in antiNodeSet:
                if extended:
                    if rows[i][j] == ".":  # Only count empty positions in extended mode
                        counter += 1
                else:
                    counter += 1

    if extended:
        # Include original antenna nodes in the count
        counter += sum(len(antennaPositions[k]) for k in antennaPositions)

    return counter

# Main function to calculate and print results
def computeAntiNodes():
    antiNodeList = []
    extendedAntiNodeList = []

    # Find anti-nodes and extended anti-nodes for each antenna type
    for k in antennaPositions:
        antiNodeList += findAntiNodes(antennaPositions[k], maxX, maxY)
        extendedAntiNodeList += findExtendedAntiNodes(antennaPositions[k], maxX, maxY)

    # Read the file again to analyze the grid
    with open("2024/D8.txt", "r") as file:
        rows = [list(r.strip("\n")) for r in file.readlines()]

    # Count normal anti-nodes
    normalCount = countAntiNodes(rows, antiNodeList, antennaPositions, extended=False)
    print("Number of Anti-Nodes:", normalCount)

    # Count extended anti-nodes (with resonance)
    extendedCount = countAntiNodes(rows, extendedAntiNodeList, antennaPositions, extended=True)
    print("Number of Anti-Nodes with Resonance:", extendedCount)

# Measure execution time
import time

start_time = time.time()  # Start the timer
computeAntiNodes()
end_time = time.time()  # End the timer
print(f"{end_time - start_time:.6f} seconds")  # Print the execution time
