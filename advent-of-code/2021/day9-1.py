dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def low_point(heightmap, i, j):
    m, n = len(heightmap), len(heightmap[0])

    for di, dj in dirs:
        if 0 <= i + di < m and 0 <= j + dj < n:
            if heightmap[i][j] >= heightmap[i + di][j + dj]:
                return False

    return True

def solve(heightmap):
    total = 0

    for i, row in enumerate(heightmap):
        for j, cell in enumerate(row):
            if low_point(heightmap, i, j):
                total += heightmap[i][j] + 1

    return total

def main():
    with open("input/9.data") as f:
        heightmap = [[int(x) for x in line.strip()] for line in f.readlines()]
        print(solve(heightmap))

if __name__ == "__main__":
    main()
