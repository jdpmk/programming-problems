def seek(g, v, i, j, m, n):
    while j >= 0 and g[i][j].isdigit() and not v[i][j]:
        v[i][j] = True
        j -= 1
    j += 1

    total = 0
    while j < n and g[i][j].isdigit():
        v[i][j] = True
        total = 10 * total + int(g[i][j])
        j += 1

    return total

def symbol(c):
    return c != '.' and not c.isdigit()

def solve(g):
    m, n = len(g), len(g[0])
    v = [[False for _ in range(n)] for _ in range(m)]

    total = 0
    for i in range(m):
        for j in range(n):
            if symbol(g[i][j]):
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if not di and not dj: continue
                        i_ = i + di
                        j_ = j + dj
                        if not v[i_][j_] and g[i_][j_].isdigit():
                            total += seek(g, v, i_, j_, m, n)

    return total

def main():
    with open("input/3.data") as f:
        schematic = [line.strip() for line in f.readlines()]
        print(solve(schematic))

if __name__ == "__main__":
    main()
