with open("2015\D2.txt", "r")as file:
    sommaCarta = 0
    sommaRibbon = 0
    for riga in file:
        x,y,z =list(map(int, riga.strip("\n").split("x")))

        sommaCarta += 2*(x*y + y*z + x*z) + min(x*y, y*z, x*z)

        lista = [x, y, z]
        lista.sort()
        lista = lista[:2]
        sommaRibbon += 2*sum(lista) + x*y*z

print(sommaCarta)
print(sommaRibbon)