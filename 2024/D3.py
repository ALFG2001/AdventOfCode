def mul(a, b):
    return a * b

def calculate_multiplications():
    with open("2024\\D3.txt", "r") as file:
        line = file.read()

    index = 0
    sum_mul_part1 = 0
    enabled = True
    sum_mul_part2 = 0

    while index != -1:
        do_index = line.find("do()", index)
        dont_index = line.find("don't()", index)
        mul_index = line.find("mul(", index)

        next_index = min((i for i in [do_index, dont_index, mul_index] if i != -1), default=-1)
        if next_index == -1:
            break

        if next_index == do_index:
            enabled = True
            index = do_index + 4

        elif next_index == dont_index:
            enabled = False
            index = dont_index + 7

        elif next_index == mul_index:
            start = mul_index + 4
            end = line.find(")", start)
            if end != -1:
                params = line[start:end].split(",")
                if len(params) == 2 and all(p.strip().isdigit() for p in params):
                    if enabled:
                        sum_mul_part2 += eval(line[mul_index:end+1])
                    sum_mul_part1 += eval(line[mul_index:end+1])

            index = mul_index + 4

    print("Total of the multiplications:", sum_mul_part1)
    print("Total of the enabled multiplications:", sum_mul_part2)


import time

start_time = time.time()
calculate_multiplications()
end_time = time.time()
print(f"{end_time - start_time:.6f} seconds")
