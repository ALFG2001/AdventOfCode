def parte1():
    SommaSafe = 0

    with open("2024\D2.txt", "r") as reports:
        for riga in reports:
            livelli = map(int, riga.strip("\n").split(" "))
            livelli = list(livelli)

            safe = True
            if sorted(livelli) == livelli or sorted(livelli, reverse=True) == livelli:
                for i in range(len(livelli)-1):
                    if abs(livelli[i] - livelli[i+1]) not in [1,2,3]:
                        safe = False
                        break
            else:
                safe = False
                
            if safe:
                SommaSafe += 1

    print("Somma report safe:",SommaSafe)

def parte2():
    SommaSafe = 0

    with open("2024\D2.txt", "r") as reports:
        for riga in reports:
            livelli = list(map(int, riga.strip("\n").split(" ")))

            for indice in range(len(livelli)):
                livelliDampened = livelli[0:indice]+livelli[indice+1:len(livelli)]

                safe = True
                if sorted(livelliDampened) == livelliDampened or sorted(livelliDampened, reverse=True) == livelliDampened:
                    for i in range(len(livelliDampened)-1):
                        if abs(livelliDampened[i] - livelliDampened[i+1]) not in [1,2,3]:
                            safe = False
                            break
                else:
                    safe = False

                if safe:
                    SommaSafe += 1
                    break

    print("Somma report safe (dampened):",SommaSafe)   

print("02-12-2024")
parte1()     
parte2()