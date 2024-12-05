def trovaXMAS(lettere, parola):
    direzioni = [
        (0, 1),  # Destra
        (0, -1), # Sinistra
        (1, 0),  # Sotto
        (-1, 0), # Sopra
        (1, 1),  # Diagonale basso-destra
        (-1, -1),# Diagonale alto-sinistra
        (-1, 1), # Diagonale alto-destra
        (1, -1)  # Diagonale basso-sinistra
    ]
    parola_len = len(parola)
    count = 0

    for i in range(len(lettere)):
        for j in range(len(lettere[i])):
            for dx, dy in direzioni:
                # Controlla se la parola può essere trovata in questa direzione
                if all(
                    0 <= i + k * dx < len(lettere) and
                    0 <= j + k * dy < len(lettere[0]) and
                    lettere[i + k * dx][j + k * dy] == parola[k]
                    for k in range(parola_len)
                ):
                    count += 1
    return count    

def verifica_x_mas(lettere, i, j):
    # Verifica che le coordinate siano valide
    if not (0 <= i - 1 < len(lettere) and 0 <= i + 1 < len(lettere) and 
            0 <= j - 1 < len(lettere[0]) and 0 <= j + 1 < len(lettere[0])):
        return False
    
    if lettere[i][j] != 'A':
        return False

    # Controlla i 4 casi
    caso1 = (
        lettere[i - 1][j - 1] == 'S' and lettere[i - 1][j + 1] == 'M' and
        lettere[i + 1][j - 1] == 'S' and lettere[i + 1][j + 1] == 'M'
    )
    caso2 = (
        lettere[i - 1][j - 1] == 'S' and lettere[i - 1][j + 1] == 'S' and
        lettere[i + 1][j - 1] == 'M' and lettere[i + 1][j + 1] == 'M'
    )
    caso3 = (
        lettere[i - 1][j - 1] == 'M' and lettere[i - 1][j + 1] == 'S' and
        lettere[i + 1][j - 1] == 'M' and lettere[i + 1][j + 1] == 'S'
    )
    caso4 = (
        lettere[i - 1][j - 1] == 'M' and lettere[i - 1][j + 1] == 'M' and
        lettere[i + 1][j - 1] == 'S' and lettere[i + 1][j + 1] == 'S'
    )

    return caso1 or caso2 or caso3 or caso4

def trovaCroce(lettere):
    count = 0
    for i in range(len(lettere)):
        for j in range(len(lettere[i])):
            if verifica_x_mas(lettere, i, j):
                count += 1
    return count


def parte1():
    lettere = []
    with open("2024\D4.txt.txt", "r") as file:
        for riga in file:
            letteraRiga = [l for l in riga.strip("\n")]
            lettere.append(letteraRiga)

    parola = "XMAS"
    total_occurrences = trovaXMAS(lettere, parola)
    print(f"La parola '{parola}' appare {total_occurrences} volte.")

def parte2():
    lettere = []
    with open("2024\D4.txt.txt", "r") as file:
        for riga in file:
            letteraRiga = [l for l in riga.strip("\n")]
            lettere.append(letteraRiga)

    parola = "MAS"
    total_occurrences = trovaCroce(lettere)
    print(f"La parola '{parola}' appare {total_occurrences} volte.")

print("04-12-2024")
parte1()     
parte2()