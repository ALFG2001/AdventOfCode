with open("2015\D1.txt", "r") as file:
    riga = file.read().strip("\n")

    print(riga.count("(") - riga.count(")"))

    contatore = 0
    for i in range(len(riga)):
        match riga[i]:
            case "(":
                contatore += 1
            case ")":
                contatore -= 1

        if contatore < 0:
            print(i+1)
            break