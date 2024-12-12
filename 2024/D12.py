with open("2024/D12.txt") as file:
    INPUT = file.read()

def grid(s):
    for r, row in enumerate(s.splitlines()):
        for c, char in enumerate(row):
            yield (r, c), char


def parse(inp):
    return {p: kind for p, kind in grid(inp)}


def neighbors(pt):
    r, c = pt
    return {(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)}


def regions(plot):
    been = set()
    rgns = []
    for pt, kind in plot.items():
        if pt in been:
            continue
        region = set()

        to_explore = [pt]
        while to_explore:
            p = to_explore.pop()
            region.add(p)
            for n in neighbors(p):
                if n in region:
                    continue
                if plot.get(n) == kind:
                    to_explore.append(n)

        rgns.append(region)

        been.update(region)
    return rgns


area = len


def perimeter(region):
    perim = 0
    for pt in region:
        for n in neighbors(pt):
            perim += n not in region
    return perim


def p1(inp):
    plot = parse(inp)
    return sum(area(region) * perimeter(region) for region in regions(plot))


def p2(inp):
    plot = parse(inp)
    return sum(area(region) * sides(region) for region in regions(plot))


def sides(region):
    min_r = min(r for r, c in region)
    max_r = max(r for r, c in region)
    min_c = min(c for r, c in region)
    max_c = max(c for r, c in region)

    total = 0

    edges = dict()
    for row in range(min_r, max_r + 1):
        prev_in = False
        next_edges = dict()
        for col in range(min_c, max_c + 2):
            if ((row, col) in region) != prev_in:
                prev_in = not prev_in
                next_edges[col] = prev_in
                if edges.get(col) != prev_in:
                    total += 1
        edges = next_edges

    edges = dict()
    for col in range(min_c, max_c + 1):
        prev_in = False
        next_edges = dict()
        for row in range(min_r, max_r + 2):
            if ((row, col) in region) != prev_in:
                prev_in = not prev_in
                next_edges[row] = prev_in
                if edges.get(row) != prev_in:
                    total += 1
        edges = next_edges

    return total


if __name__ == "__main__":
    print(p1(INPUT))
    print(p2(INPUT))
