import itertools

def generatePermutations(n, operatorList):
    return itertools.product(operatorList, repeat=n)

def calculateNumber(target, factors, opList):
    permutations = generatePermutations(len(factors)-1, opList)

    for perm in permutations:
        num = factors[0]
        
        for i, op in enumerate(perm):
            if op == "+":
                num += factors[i + 1]
            elif op == "*":
                num *= factors[i + 1]
            elif op == "||":
                num = int(str(num) + str(factors[i+1]))

            if num > target:
                break
            
        if num == target:
            return target
    
    return 0
    
def calculateOperations():
    equations = []
    with open("2024/D7.txt", "r") as file:
        for line in file:
            lineSplit = line.strip("\n").split(": ")
            target= int(lineSplit[0])
            factors = lineSplit[1].split(" ")
            equations.append((target,list(map(int, factors))))


    sumCorrect = 0
    for t, f in equations:
        sumCorrect += calculateNumber(t, f, ["+", "*"])

    print(sumCorrect)

    sumCorrect2 = 0
    for t, f in equations:
        sumCorrect2 += calculateNumber(t, f, ["+","*", "||"])

    print(sumCorrect2)

import time

start_time = time.time()
calculateOperations()
end_time = time.time()
print(f"{end_time - start_time:.6f} seconds")