def calculate_distances_and_similarity():
    # Initialize empty lists to hold the star pairs and variables for total distance and similarity score
    list1 = []
    list2 = []
    totalDist = 0
    simScore = 0

    # Open the file "2024\D1.txt" in read mode to process the star pairs
    with open("2024\\D1.txt", "r") as stars:
        for pair in stars:
            # Split each line into two integers, representing two stars, and add them to the lists
            star1, star2 = map(int, pair.strip("\n").split())
            list1.append(star1)
            list2.append(star2)

    # Sort both lists to align the stars in ascending order for distance calculation
    list1.sort()
    list2.sort()

    # Calculate the total distance by finding the absolute difference between corresponding stars
    for i in range(len(list1)):
        totalDist += abs(list1[i] - list2[i])

    # Calculate the similarity score by summing the product of common star values in both lists
    for star in list1:
        simScore += star * list2.count(star)

    # Output the total distance and similarity score
    print("Total Distance:", totalDist)
    print("Similarity Score:", simScore)


import time

# Measure the execution time of the function
start_time = time.time()
calculate_distances_and_similarity()
end_time = time.time()

# Print the elapsed time in seconds
print(f"{end_time - start_time:.6f} seconds")
