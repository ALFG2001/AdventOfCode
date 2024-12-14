
import numpy as np

with open("2024/D13.txt", "r") as file:
    righe = file.read().split("\n")
    premi = []
    for i in range(0,len(righe),4):
        premi.append([righe[i],righe[i+1],righe[i+2]])

def leggiStringa(stringa, sep):
    dati = stringa.split(":")[1].strip()

    parti = dati.split(", ")

    x = int(parti[0].split(sep)[1])
    y = int(parti[1].split(sep)[1])
    return x, y

def calcolaMosse(x1,x2,y1,y2, targetX, targetY, tolerance =1e-2):
    A = np.array([[x1, x2],
                [y1, y2]])

    b = np.array([targetX, targetY])

    x, y = np.linalg.solve(A, b)

    if abs(x - round(x)) < tolerance and abs(y - round(y)) < tolerance:
        return round(x), round(y)
    else:
        return None, None

def calcolaGettoni():
    gettoni1 = 0
    gettoni2 = 0
    for claw in premi:
        for i, riga in enumerate(claw):
            match i:
                case 0:
                    x1, y1 = leggiStringa(riga, "+")
                case 1:
                    x2, y2 = leggiStringa(riga, "+")
                case 2:
                    tx, ty = leggiStringa(riga, "=")

        buttonA, buttonB = calcolaMosse(x1, x2, y1, y2, tx, ty)
        if buttonA != None or buttonB != None:
            gettoni1 += buttonA*3 + buttonB

        buttonA, buttonB = calcolaMosse(x1, x2, y1, y2, tx+10000000000000, ty+10000000000000)
        if buttonA != None or buttonB != None:
            gettoni2 += buttonA*3 + buttonB
        
    print("Numero gettoni p1:",gettoni1)
    print("Numero gettoni p2:",gettoni2)


# Measure execution time
import time

start_time = time.time()  # Start the timer
calcolaGettoni()  # Call the function
end_time = time.time()  # End the timer
print(f"{end_time - start_time:.6f} seconds")  # Print the execution time
