def mul(a,b):
    return a * b

def parte1():
    with open("2024\D3.txt", "r") as file:
        riga = file.read()
    
    index = 0
    sum_mul = 0

    while index != -1:
        mul_index = riga.find("mul(", index)

        if mul_index == -1:
            break
        
        start = mul_index + 4
        end = riga.find(")", start)
        if end != -1:
            params = riga[start:end].split(",")
            if len(params) == 2 and all(p.strip().isdigit() for p in params):
                sum_mul += eval(riga[mul_index:end+1])
            index = mul_index + 4

    print("Somma delle moltiplicazioni:",sum_mul)

def parte2():
    with open("2024\D3.txt", "r") as file:
        riga = file.read()
    
    index = 0
    enabled = True
    sum_mul = 0

    while index != -1:
        do_index = riga.find("do()", index)
        dont_index = riga.find("don't()", index)
        mul_index = riga.find("mul(", index)

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
            if enabled:
                start = mul_index + 4
                end = riga.find(")", start)
                if end != -1:
                    params = riga[start:end].split(",")
                    if len(params) == 2 and all(p.strip().isdigit() for p in params):
                        sum_mul += eval(riga[mul_index:end+1])

            index = mul_index + 4

    print("Somma delle moltiplicazioni abilitate:",sum_mul)

print("03-12-2024")
parte1()    
parte2()