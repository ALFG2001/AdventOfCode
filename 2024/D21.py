from collections import deque

# Funzione per trovare i vicini di una cella
def find_neighbors(x, y):
    return {
        (x + 1, y): ">",  # Destra
        (x - 1, y): "<",  # Sinistra
        (x, y + 1): "v",  # Giù
        (x, y - 1): "^"   # Su
    }

# Funzione per verificare se una cella è valida (dentro i limiti e non vuota)
def is_valid(coord, grid, rows, cols):
    x, y = coord
    return 0 <= x < cols and 0 <= y < rows and grid[y][x] != ""

# Funzione BFS per trovare il percorso con priorità a limitare le curve
def find_path(grid, start_coord, end_coord, rows, cols):
    # Inizializzazione della coda per BFS e dizionario di visitati
    visited = {}
    queue = deque([(start_coord, None, 0)])  # (coord, direzione precedente, penalità)

    while queue:
        current, prev_direction, penalty = queue.popleft()

        if current == end_coord:
            break  # Percorso trovato

        for neighbor, direction in find_neighbors(*current).items():
            if neighbor not in visited and is_valid(neighbor, grid, rows, cols):
                # Calcola la penalità per il cambio di direzione
                new_penalty = penalty + (1 if prev_direction and prev_direction != direction else 0)
                queue.append((neighbor, direction, new_penalty))
                visited[neighbor] = (current, direction, new_penalty)

    # Se il percorso non è stato trovato
    if end_coord not in visited:
        return False

    # Ricostruzione del percorso
    path = []
    current = end_coord
    while current != start_coord:
        prev, direction, _ = visited[current]
        path.append(direction)
        current = prev

    return path[::-1]  # Restituiamo il percorso inverso

# Caricamento dei codici dal file
with open("2024/D21.txt") as file:
    codes = [riga.strip("\n") for riga in file]

# Definizione delle matrici di numeri e frecce
num_keypad = [["7", "8", "9"],
              ["4", "5", "6"],
              ["1", "2", "3"],
              ["", "0", "A"]]

arrow_keypad = [["", "^", "A"],
                ["<", "v", ">"]]

# Creazione dei dizionari per le coordinate
coordinate_num = {value: (j, i) for i, row in enumerate(num_keypad) for j, value in enumerate(row) if value}
coordinate_arrow = {value: (j, i) for i, row in enumerate(arrow_keypad) for j, value in enumerate(row) if value}

def calcola(stringa, diz_coord, grid):
    path = []
    start = diz_coord["A"]
    for dir in stringa:
        end = diz_coord[dir]
        path.extend(find_path(grid, start, end, len(grid), len(grid[0])))
        path.append("A")
        start = end
    return path

# Funzione per calcolare il percorso per il primo livello
p1 = {}
for code in codes:
    path = calcola(code, coordinate_num, num_keypad)
    p1[code] = "".join(path)

# Funzione per calcolare il percorso per il secondo livello
p2 = {}
for k, value in p1.items():
    path = calcola(value, coordinate_arrow, arrow_keypad)
    p2[k] = "".join(path)

# Funzione per calcolare il percorso per il terzo livello
p3 = {}
start = coordinate_arrow["A"]
for k, value in p2.items():
    path = calcola(value, coordinate_arrow, arrow_keypad)
    p3[k] = "".join(path)


k = "029A"
print(k , p1[k], len(p1[k]))
print(k , p2[k], len(p2[k]))
print(k , p3[k], len(p3[k]))

print(len(calcola("v<<A>>^A<A>A<AA>vA^A<vAAA>^A",coordinate_arrow, arrow_keypad)))