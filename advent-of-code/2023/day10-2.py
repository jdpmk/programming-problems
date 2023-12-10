import collections

def solve(g):
    m, n = len(g), len(g[0])

    def in_bounds(i, j):
        return 0 <= i < m and 0 <= j < n

    def horz(i, j, from_right):
        return in_bounds(i ,j) and \
               g[i][j] in ("-LF" if from_right else "-J7")

    def vert(i, j, from_bottom):
        return in_bounds(i ,j) and \
               g[i][j] in ("|7F" if from_bottom else "|LJ")

    def deduce(i, j):
        if vert(i - 1, j, True) and vert(i + 1, j, False): return "|"
        if horz(i, j - 1, True) and horz(i, j + 1, False): return "-"
        if horz(i, j + 1, False) and vert(i - 1, j, True): return "L"
        if horz(i, j - 1, True) and vert(i - 1, j, True): return "J"
        if horz(i, j - 1, True) and vert(i + 1, j, False): return "7"
        if horz(i, j + 1, False) and vert(i + 1, j, False): return "F"
        assert False, "Unknown pipe configuration"

    def get_start():
        for i in range(m):
            for j in range(n):
                if g[i][j] == "S":
                    return i, j
        assert False, "No starting position found"

    def get_adj(i, j):
        if g[i][j] == "|": return [(i - 1, j), (i + 1, j)]
        if g[i][j] == "-": return [(i, j - 1), (i, j + 1)]
        if g[i][j] == "L": return [(i - 1, j), (i, j + 1)]
        if g[i][j] == "J": return [(i - 1, j), (i, j - 1)]
        if g[i][j] == "7": return [(i, j - 1), (i + 1, j)]
        if g[i][j] == "F": return [(i, j + 1), (i + 1, j)]
        assert False, "Unknown pipe symbol: {}".format(g[i][j])

    i, j = get_start()
    g[i][j] = deduce(i, j)

    q = collections.deque([(i, j)])
    vis = set([(i, j)])
    while q:
        c = q.popleft()
        adj = [a for a in get_adj(*c) if a not in vis]
        for a in adj:
            vis.add(a)
            q.append(a)

    total = 0
    for i in range(m):
        enclosed = False
        last = None
        for j in range(n):
            if (i, j) in vis:
                if g[i][j] == "|":
                    enclosed = not enclosed
                elif last is not None and \
                     (last, g[i][j]) in [("F", "J"), ("L", "7")]:
                    enclosed = not enclosed
                if g[i][j] != "-":
                    last = g[i][j]
            if enclosed and (i, j) not in vis:
                total += 1

    return total

def main():
    with open("input/10.data") as f:
        g = [list(line.strip()) for line in f.readlines()]
        print(solve(g))

if __name__ == "__main__":
    main()
