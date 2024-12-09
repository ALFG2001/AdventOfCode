def organizeDisk():
    # Open the file and read its contents
    with open("2024/D9.txt", "r") as file:
        data = file.read().strip("\n")  # Read the file content and remove trailing newline

    disk_list = []  # List to store the disk content
    index = 0  # Variable to track the disk number (e.g., 0, 1, 2, ...)
    total_length = 0  # To track the total length of non-dot elements

    # Process the string data from the file
    for i, n in enumerate(data):
        if i % 2 == 0:
            # Create a list of 'x' repeated `n` times
            sublist = [index for _ in range(int(n))]
            disk_list += sublist  # Add the sublist to the main list
            total_length += len(sublist)  # Increase total length
            index += 1  # Increment the disk number
        else:
            # Add a list of dots (".") repeated `n` times
            disk_list += ["." for _ in range(int(n))]

    left = 0  # Left pointer for the processing
    right = len(disk_list) - 1  # Right pointer for the processing
    output_list = []  # List to store the final output

    # Reorder the disk list by swapping elements
    while True:
        # Move left pointer to the right until we find a non-dot element
        while disk_list[left] != ".":
            output_list.append(disk_list[left])
            left += 1

        # Move right pointer to the left until we find a non-dot element
        while disk_list[right] == ".":
            right -= 1

        # If the left pointer is less than the right pointer, swap the elements
        if left < right:
            disk_list[left], disk_list[right] = disk_list[right], disk_list[right]
            output_list.append(disk_list[left])  # Append the swapped element to the output
            left += 1  # Move the left pointer
            right -= 1  # Move the right pointer
        else:
            break

    output_list = output_list[:total_length]  # Trim the list to the correct length

    # Calculate the checksum for the output list
    checksum = 0
    for i, n in enumerate(output_list):
        checksum += i * n  # Multiply index by the value of the element

    print("Checksum:", checksum)  # Print the checksum

    disk_list = []  # Reinitialize the disk list
    index = 0  # Reset the disk number

    # Recreate the disk list using the original data string
    for index_disk, n in enumerate(data):
        if index_disk % 2 == 0:
            sublist = [str(index) for _ in range(int(n))]
            disk_list.append(sublist)  # Add the sublist to the disk list
            index += 1  # Increment the disk number
        else:
            dot_list = [a for a in ["." for _ in range(int(n))]]
            if dot_list:
                disk_list.append(dot_list)  # Add the dot list to the disk list

    unified_list = []  # List to store the unified elements

    # Variable to track the current element for grouping
    current_element = None
    count = 0  # Variable to count consecutive occurrences of the same element

    # Iterate through the disk list and group consecutive identical elements
    for element in disk_list:
        if element == current_element:
            count += 1  # Increment the count for consecutive identical elements
        else:
            if current_element is not None:
                unified_list.append(current_element * count)  # Add the group of repeated elements to the unified list
            current_element = element  # Update the current element
            count = 1  # Reset the count

    # Add the last group of repeated elements
    if current_element is not None:
        unified_list.append(current_element * count)

    unified_list = [item for sublist in unified_list for item in sublist]  # Flatten the unified list

    right = len(unified_list) - 1  # Reset the right pointer
    left = 0  # Reset the left pointer
    target = unified_list[right]  # Set the target to the last element

    # Reorder the unified list based on conditions
    while right > 0:
        # Move the right pointer to find the last non-dot element
        while unified_list[right] == ".":
            right -= 1

        target = unified_list[right]  # Update the target
        end = right + 1  # Set the end position

        # Move the right pointer to find the end of the group of identical elements
        while unified_list[right] == target:
            right -= 1

        left = 0  # Reset the left pointer
        switch = False  # Flag to indicate if a swap is needed

        # Process the list to find elements that need swapping
        while True:
            # Move the left pointer to find the next dot
            while unified_list[left] != ".":
                left += 1

            if left > right:
                break

            start = left

            # Move the left pointer to find the next non-dot element
            while unified_list[left] == ".":
                left += 1

            # If the length of the dots between left and right is larger, mark for swapping
            if len(unified_list[start:left]) >= len(unified_list[right + 1:end]):
                switch = True
                break

        # Perform the swap if needed
        if switch:
            for i in range(right + 1, end):
                unified_list[start], unified_list[i] = unified_list[i], unified_list[start]
                start += 1

        # Move the right pointer if it is pointing to a dot
        if unified_list[right] == ".":
            right -= 1

    # Calculate the optimized checksum
    optimized_checksum = 0
    for i, num in enumerate(unified_list):
        if num.isdigit():
            optimized_checksum += int(num) * i  # Multiply index by the numeric value of the element

    print("Optimized Checksum:", optimized_checksum)  # Print the optimized checksum


# Measure execution time
import time

start_time = time.time()  # Start the timer
organizeDisk()  # Call the function
end_time = time.time()  # End the timer
print(f"{end_time - start_time:.6f} seconds")  # Print the execution time
