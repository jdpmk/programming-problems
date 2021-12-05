def solve(coords):
    n = 0

    for coord in coords:
        (x1, y1), (x2, y2) = coord
        n = max(n, x1, y1, x2, y2) + 1

    grid = [[0 for _ in range(n)] for _ in range(n)]

    for coord in coords:
        (x1, y1), (x2, y2) = coord

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[x][y1] += 1

    ct = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2:
                ct += 1

    return ct

def main():
    with open("input/5.data") as f:
        coords = [[(tuple(map(int, pair.split(",")))) for pair in line.strip().split(" -> ")] for line in f.readlines()]
        print(solve(coords))

if __name__ == "__main__":
    main()
