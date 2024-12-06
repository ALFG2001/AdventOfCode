def muovi(simbolo, posX, posY, listaCaselle, setCaselle: set):

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

    # Restituisci False per indicare che il movimento è avvenuto
    return False, newX, newY, simbolo

caselle = []
caselle2 = []
ostacoli = []

collezionePercorsi = []


y = 0
caselleUniche = set()

trovato = False
with open("2024/D6.txt", "r") as file:
    for riga in file:
        caselle.append([c for c in riga.strip("\n")])
        
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


# Stampa la griglia aggiornata e le caselle uniche visitate
for riga in caselle:
    print("".join(riga))
print(len(caselleUniche))

print(ostacoli)