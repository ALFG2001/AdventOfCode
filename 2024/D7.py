import itertools

# Function to generate permutations of operators for the given length
def generatePermutations(n, operatorList):
    # Generate all possible combinations of operators with length 'n'
    return itertools.product(operatorList, repeat=n)

# Function to calculate the result based on target and factors with a list of operators
def calculateNumber(target, factors, opList):
    # Generate all possible operator permutations for the given factors (one less than number of factors)
    permutations = generatePermutations(len(factors)-1, opList)

    # Iterate through all the operator permutations
    for perm in permutations:
        num = factors[0]  # Start with the first factor

        # Apply each operator from the permutation to the corresponding factor
        for i, op in enumerate(perm):
            if op == "+":
                num += factors[i + 1]  # Add the next factor
            elif op == "*":
                num *= factors[i + 1]  # Multiply by the next factor
            elif op == "||":
                num = int(str(num) + str(factors[i+1]))  # Concatenate numbers (for "||")

            # If the number exceeds the target, break out of the loop to try the next permutation
            if num > target:
                break
            
        # If the resulting number matches the target, return it
        if num == target:
            return target
    
    # If no permutation gives the target number, return 0
    return 0
    
# Function to calculate and sum the correct answers for all equations
def calculateOperations():
    equations = []  # List to store the equations

    # Open and read the input file
    with open("2024/D7.txt", "r") as file:
        # Iterate through each line in the file
        for line in file:
            lineSplit = line.strip("\n").split(": ")  # Split target and factors
            target = int(lineSplit[0])  # Convert the target to an integer
            factors = lineSplit[1].split(" ")  # Split the factors as a list of strings
            equations.append((target, list(map(int, factors))))  # Store the target and factors as a tuple
    
    # Calculate the sum of correct results using the operators "+" and "*"
    sumCorrect = 0
    for t, f in equations:
        sumCorrect += calculateNumber(t, f, ["+", "*"])

    # Print the sum for the first calculation
    print("Correct equations:",sumCorrect)

    # Calculate the sum of correct results using the operators "+", "*", and "||"
    sumCorrect2 = 0
    for t, f in equations:
        sumCorrect2 += calculateNumber(t, f, ["+", "*", "||"])

    # Print the sum for the second calculation
    print("Correct equations with pipe:",sumCorrect2)

# Measure the execution time of the function
import time

start_time = time.time()  # Start the timer
calculateOperations()  # Call the function to perform the calculations
end_time = time.time()  # End the timer
print(f"{end_time - start_time:.6f} seconds")  # Print the execution time in seconds
