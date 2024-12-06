def muovi(simbolo, posX, posY, listaCaselle, setCaselle: set):
    global caselleCronologiche
    # Determina la direzione di movimento e la rotazione a destra
    match simbolo:
        case "^":
            spostamento = [0, -1]
            destra = ">"
        case "v":
            spostamento = [0, +1]
            destra = "<"
        case ">":
            spostamento = [+1, 0]
            destra = "v"
        case "<":
            spostamento = [-1, 0]
            destra = "^"

    # Calcola le nuove coordinate
    newY = posY + spostamento[1]
    newX = posX + spostamento[0]

    # Controlla i confini della griglia
    if newY < 0 or newY >= len(listaCaselle) or newX < 0 or newX >= len(listaCaselle[0]):
        return True, newX, newY, simbolo  # Movimento fuori dai confini

    # Recupera la casella target
    casellaTarget = listaCaselle[newY][newX]

    # Se la casella è un muro, gira a destra e prova di nuovo
    if casellaTarget == "#":
        return muovi(destra, posX, posY, listaCaselle, setCaselle)

    # Aggiorna la posizione e segna la casella visitata
    listaCaselle[posY][posX] = "X"  # Segna la vecchia posizione come visitata
    listaCaselle[newY][newX] = simbolo  # Aggiorna la nuova posizione con il simbolo
    setCaselle.add((newX, newY))  # Registra la nuova posizione visitata
    caselleCronologiche.append((newX,newY, simbolo))
    # Restituisci False per indicare che il movimento è avvenuto
    return False, newX, newY, simbolo

def muoviLoop(simbolo, posX, posY, listaCaselle, history: set):
    # Determina la direzione di movimento e la rotazione a destra
    match simbolo:
        case "^":
            spostamento = [0, -1]
            destra = ">"
        case "v":
            spostamento = [0, +1]
            destra = "<"
        case ">":
            spostamento = [+1, 0]
            destra = "v"
        case "<":
            spostamento = [-1, 0]
            destra = "^"

    # Calcola le nuove coordinate
    newY = posY + spostamento[1]
    newX = posX + spostamento[0]

    # Controlla i confini della griglia
    if newY < 0 or newY >= len(listaCaselle) or newX < 0 or newX >= len(listaCaselle[0]):
        return True, newX, newY, simbolo, False  # Movimento fuori dai confini

    # Recupera la casella target
    casellaTarget = listaCaselle[newY][newX]

    # Se la casella è un muro, gira a destra e prova di nuovo
    if casellaTarget == "#":
        return muoviLoop(destra, posX, posY, listaCaselle, history)

    # Controlla se lo stato attuale (posizione e direzione) è già stato visitato
    

    # Aggiorna la posizione e segna la casella visitata
    listaCaselle[posY][posX] = "X"  # Segna la vecchia posizione come visitata
    listaCaselle[newY][newX] = simbolo  # Aggiorna la nuova posizione con il simbolo

    stato_attuale = (newX, newY, simbolo)
    if stato_attuale in history:
        return True, newX, newY, simbolo, True  # Loop infinito rilevato

    # Aggiungi lo stato attuale alla cronologia
    history.add(stato_attuale)

    # Restituisci False per indicare che il movimento è avvenuto senza loop
    return False, newX, newY, simbolo, False


caselle = []
caselle2 = []
ostacoli = []
y = 0
caselleUniche = set()
caselleCronologiche = []

trovato = False
with open("2024/D6.txt", "r") as file:
    for riga in file:
        caselle.append([c for c in riga.strip("\n")])
        caselle2.append([c if c in '.#' else '.' for c in riga.strip("\n")])
        try:
            x = riga.index("^")
            start = (x, y)
        except ValueError:
            y += 1
        

for i in range(len(caselle)):
    for j in range(len(caselle[i])):
        if caselle[i][j] == "#":
            ostacoli.append((j,i))

esci = False
x, y = start[0], start[1]
caselleUniche.add((x,y))
simbolo = "^"
while not esci:
    esci, x, y, simbolo = muovi(simbolo, x, y, caselle, caselleUniche)

print("Caselle Uniche",len(caselleUniche))

import copy

collezioneMappe = [copy.deepcopy(caselle2) for _ in range(len(caselleCronologiche))]
xyLoop = set()



indiceMappa = 0
_ = 0


for x,y,p in caselleCronologiche:
    oX, oY = x,y

    collezioneMappe[indiceMappa][oY][oX] = "#"

    visitedStates = set()
    exitLoop = False
    loopCoordinates = None

    sx, sy = start
    p = "^"
    
    while not exitLoop:
        
        exitLoop, sx, sy, p, loopFlag = muoviLoop(
            p, sx, sy, collezioneMappe[indiceMappa], visitedStates
        )    

    if loopFlag:
        xyLoop.add((oX,oY))

    indiceMappa += 1

print("Numero Ostacoli",len(xyLoop))
