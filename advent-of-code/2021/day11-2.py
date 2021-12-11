import copy

def flash(grid, flashed, i, j):
    m, n = len(grid), len(grid[0])
    flashed[i][j] = True
    grid[i][j] = 0

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di or dj:
                i_ = i + di
                j_ = j + dj

                if 0 <= i_ < m and 0 <= j_ < n and not flashed[i_][j_]:
                    grid[i_][j_] += 1
                    if grid[i_][j_] > 9:
                        flash(grid, flashed, i_, j_)

def solve(grid):
    m, n = len(grid), len(grid[0])
    num_iterations = 100
    iteration = 1

    while True:
        cp = copy.deepcopy(grid)

        for i in range(m):
            for j in range(n):
                cp[i][j] += 1

        flashed = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if cp[i][j] > 9 and not flashed[i][j]:
                    flash(cp, flashed, i, j)

        num_flashed = 0
        for i in range(m):
            for j in range(n):
                if not cp[i][j]:
                    num_flashed += 1

        if num_flashed == m * n:
            return iteration

        iteration += 1
        grid = cp

    assert False

def main():
    with open("input/11.data") as f:
        grid = [[int(x) for x in line.strip()] for line in f.readlines()]
        print(solve(grid))

if __name__ == "__main__":
    main()
