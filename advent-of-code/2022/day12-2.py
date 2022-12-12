import collections

def solve(grid):
    m, n = len(grid), len(grid[0])

    si, sj = 0, 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "S":
                grid[i][j] = ord("a")
            elif grid[i][j] == "E":
                si, sj = i, j
                grid[i][j] = ord("z")
            else:
                grid[i][j] = ord(grid[i][j])

    q = collections.deque([(0, si, sj)])
    visited = set()

    while q:
        steps, i, j = q.popleft()
        
        if grid[i][j] == ord("a"):
            return steps

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i_ = i + di
            j_ = j + dj

            if 0 <= i_ < m and 0 <= j_ < n:
                if grid[i][j] <= grid[i_][j_] + 1:
                    if (i_, j_) not in visited:
                        visited.add((i_, j_))
                        q.append((steps + 1, i_, j_))

    return -1

def main():
    with open("input/12.data") as f:
        grid = [list(line.strip()) for line in f.readlines()]
        print(solve(grid))

if __name__ == "__main__":
    main()
