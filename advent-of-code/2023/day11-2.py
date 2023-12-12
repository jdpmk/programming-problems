def get_num_expansions(universe):
    m = len(universe)
    acc = [0] * m

    for i in range(m):
        acc[i] = acc[i - 1] if i > 0 else 0
        if all(c == "." for c in universe[i]):
            acc[i] += 999999

    return acc

def solve(universe):
    m, n = len(universe), len(universe[0])
    transposed = list(map(list, zip(*universe)))

    er = get_num_expansions(universe)
    ec = get_num_expansions(transposed)

    coords = []
    for i in range(m):
        for j in range(n):
            if universe[i][j] == "#":
                coords.append((i + er[i], j + ec[j]))

    k = len(coords)
    total = 0
    for i in range(k):
        a, b = coords[i]
        for j in range(i + 1, k):
            c, d = coords[j]
            total += abs(c - a) + abs(d - b)

    return total

def main():
    with open("input/11.data") as f:
        lines = [line.strip() for line in f.readlines()]
        print(solve(lines))

if __name__ == "__main__":
    main()
