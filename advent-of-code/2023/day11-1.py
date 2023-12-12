def expand(universe):
    def f(u):
        e = []
        for s in u:
            e.append(s)
            if all(c == "." for c in s):
                e.append(s)
        return e

    universe = f(universe)
    universe = map(list, zip(*universe))
    universe = f(universe)

    return universe

def get_coords(universe):
    coords = []
    for i, s in enumerate(universe):
        for j, c in enumerate(s):
            if c == "#":
                coords.append((i, j))
    return coords

def solve(universe):
    universe = expand(universe)
    coords = get_coords(universe)

    n = len(coords)
    total = 0
    for i in range(n):
        a, b = coords[i]
        for j in range(i + 1, n):
            c, d = coords[j]
            total += abs(c - a) + abs(d - b)

    return total

def main():
    with open("input/11.data") as f:
        lines = [line.strip() for line in f.readlines()]
        print(solve(lines))

if __name__ == "__main__":
    main()
