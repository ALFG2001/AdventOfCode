with open("2015\D3.txt", "r") as file:
    case = set()
    case2 = set()
    x, y = 0,0

    santaX, santaY = 0,0
    roboX, roboY = 0,0
    turno = True

    for direzione in file.read().strip("\n"):
        case.add((x,y))

        if turno:
            case2.add((santaX,santaY))
        else:
            case2.add((roboX,roboY))

        match direzione:
            case ">":
                x += 1
                if turno:
                   santaX += 1
                else:
                   roboX += 1
            case "<":
                x -= 1
                if turno:
                   santaX -= 1
                else:
                   roboX -= 1
            case "^":
                y += 1
                if turno:
                   santaY += 1
                else:
                   roboY += 1
            case "v":
                y -= 1
                if turno:
                   santaY -= 1
                else:
                   roboY -= 1
        case.add((x,y))
        if turno:
            case2.add((santaX,santaY))
        else:
            case2.add((roboX,roboY))

        turno = not turno

print(len(case))
print(len(case2))