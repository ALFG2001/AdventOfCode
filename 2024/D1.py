def parte1():
    lista1 = []
    lista2 = []
    sommaDist = 0

    with open("2024\D1.txt", "r") as stelle:
        for coppia in stelle:
            stella1, stella2 = map(int, coppia.strip("\n").split())
            lista1.append(stella1)
            lista2.append(stella2)

    lista1.sort()
    lista2.sort()

    for i in range(len(lista1)):
        sommaDist += abs(lista1[i] - lista2[i])

    print("Somma Distanze:",sommaDist)

def parte2():
    Lista1 = []
    lista2 = []
    simScore = 0

    with open("2024\D1.txt", "r") as stelle:
        for coppia in stelle:
            stella1, stella2 = map(int, coppia.strip("\n").split())
            Lista1.append(stella1)
            lista2.append(stella2)

    for stella in Lista1:
        simScore += stella*lista2.count(stella)

    print("Similarity Score:",simScore)

print("01-12-2024")
parte1()     
parte2()