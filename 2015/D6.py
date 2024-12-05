grid = [[0 for _ in range(1000)] for _ in range(1000)]
gridLum = [[0 for _ in range(1000)] for _ in range(1000)]

with open("2015\D6.txt", "r") as file:
    for riga in file:
        rigaSplit = riga.strip("\n").split(" ")
        if len(rigaSplit) > 4:
            on = rigaSplit[1] == "on"
            angolo1X, angolo1Y = map(int, rigaSplit[2].split(","))
            angolo2X, angolo2Y = map(int, rigaSplit[4].split(","))

            for i in range(min(angolo1Y, angolo2Y), max(angolo1Y, angolo2Y)+1):
                for j in range(min(angolo1X, angolo2X), max(angolo1X, angolo2X)+1):
                    if on:
                        grid[i][j] = 1
                        gridLum[i][j] += 1
                    else:
                        grid[i][j] = 0
                        gridLum[i][j] = max(gridLum[i][j] - 1, 0)
        else:
            angolo1X, angolo1Y = map(int, rigaSplit[1].split(","))
            angolo2X, angolo2Y = map(int, rigaSplit[3].split(","))

            for i in range(min(angolo1Y, angolo2Y), max(angolo1Y, angolo2Y)+1):
                for j in range(min(angolo1X, angolo2X), max(angolo1X, angolo2X)+1):
                        grid[i][j] = not grid[i][j]
                        gridLum[i][j] += 2


count = 0
for riga in grid:
    count += riga.count(1)

print(count)

lum = 0
for i in range(len(gridLum)):
    for j in range(len(gridLum[i])):
        lum += gridLum[i][j]

print(lum)