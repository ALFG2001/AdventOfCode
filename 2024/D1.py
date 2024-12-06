def calculate_distances_and_similarity():
    list1 = []
    list2 = []
    totalDist = 0
    simScore = 0

    with open("2024\\D1.txt", "r") as stars:
        for pair in stars:
            star1, star2 = map(int, pair.strip("\n").split())
            list1.append(star1)
            list2.append(star2)

    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        totalDist += abs(list1[i] - list2[i])

    for star in list1:
        simScore += star * list2.count(star)

    print("Total Distance:", totalDist)
    print("Similarity Score:", simScore)


import time

start_time = time.time()
calculate_distances_and_similarity()
end_time = time.time()
print(f"{end_time - start_time:.6f} seconds")
