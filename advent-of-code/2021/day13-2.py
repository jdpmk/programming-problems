def fold(grid, area, orientation, value):
    if orientation == "y":
        assert not any(grid[value])
        for i in range(value + 1, area[2] + 1):
            for j in range(area[1], area[3] + 1):
                grid[value - (i - value)][j] |= grid[i][j]

        area = (area[0], area[1], value, area[3])

    elif orientation == "x":
        assert not any([row[value] for row in grid])

        for i in range(area[0], area[2] + 1):
            for j in range(value + 1, area[3] + 1):
                grid[i][value - (j - value)] |= grid[i][j]

        area = (area[0], area[1], area[2], value)

    else:
        assert False

    return grid, area

def solve(n, dots, folds):
    area = (0, 0, n - 1, n - 1)
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for i, j in dots:
        grid[j][i] = 1

    for orientation, value in folds:
        grid, area = fold(grid, area, orientation, value)

    for i in range(area[0], area[2] + 1):
        for j in range(area[1], area[3] + 1):
            print('#' if grid[i][j] else '.', end='')
        print()

def main():
    with open("input/13.data") as f:
        contents = "".join(f.readlines())
        dots, folds = contents.split("\n\n")
        n = 0

        dots_ = []
        for pair in dots.split("\n"):
            i, j = pair.split(",")
            dots_.append((int(i), int(j)))
            n = max(n, int(i), int(j)) + 1

        folds_ = []
        for fold in folds.split("\n"):
            orientation, value = fold.split("=")
            folds_.append((orientation[-1], int(value)))

        solve(n, dots_, folds_)

if __name__ == "__main__":
    main()
