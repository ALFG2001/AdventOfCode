import time

def checkCorretta(dizionario, riga):
    for i in range(len(riga)):
        if riga[i] in dizionario:
            prima = riga[:i]
            for checkNum in prima:
                if checkNum in dizionario[riga[i]]:
                    return False
    return True

def correggiLista(dizionario, listaNonCorretta):
    for i in range(1, len(listaNonCorretta)):
        elemento_corrente = listaNonCorretta[i]
        
        if elemento_corrente in dizionario:
            parte_iniziale = listaNonCorretta[:i]
            parte_finale = listaNonCorretta[i + 1:]

            for j in range(len(parte_iniziale)):
                elemento_iniziale = parte_iniziale[j]
                
                if elemento_iniziale in dizionario[elemento_corrente]:
                    nuovaLista = (
                        parte_iniziale[:j] + 
                        [elemento_corrente, elemento_iniziale] + 
                        parte_iniziale[j + 1:] + 
                        parte_finale
                    )

                    if not checkCorretta(dizionario, nuovaLista):
                        soluzione = correggiLista(dizionario, nuovaLista)
                        if soluzione:
                            return soluzione
                    else:
                        return nuovaLista
    
s = time.time()    
ruleset = []
rows = []
dictPages = {}
midSum = 0
midSumCorretta = 0

with open("2024\D5.txt", "r") as file:
    for riga in file:
        if "|" in riga:
            ruleset.append(riga.strip("\n"))
        elif "," in riga:
            rows.append(riga.strip("\n"))
                        
for riga in ruleset:
    numPrima, numDopo = riga.split("|")
    if numPrima not in dictPages:
        dictPages[numPrima] = [numDopo]
    else:
        dictPages[numPrima].append(numDopo)

for riga in rows:
    listaNum = riga.split(",")
    corretto = checkCorretta(dictPages, listaNum)
    
    if corretto:
        midSum += int(listaNum[len(listaNum)//2])
    else:
        listaCorretta = correggiLista(dictPages, listaNum)
        midSumCorretta += int(listaCorretta[len(listaCorretta)//2])
                     
print(midSum)
print(midSumCorretta)
e = time.time()

print(f"{e-s:.6f} seconds")