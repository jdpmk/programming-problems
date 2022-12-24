import collections

def solve(grid):
    m, n = len(grid), len(grid[0])

    def wall(i, j):
        return j == 0 or j == n - 1 or (i == 0 and j != 1) or (i == m - 1 and j != n - 2)

    def initialize():
        g = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] in "^v<>":
                    g.append((grid[i][j], i, j))
        return g

    def advance(g):
        g_ = []
        for x, i, j in g:
            if x == "^": g_.append((x, *((m - 2, j) if wall(i - 1, j) else (i - 1, j))))
            if x == "v": g_.append((x, *((1, j) if wall(i + 1, j) else (i + 1, j))))
            if x == "<": g_.append((x, *((i, n - 2) if wall(i, j - 1) else (i, j - 1))))
            if x == ">": g_.append((x, *((i, 1) if wall(i, j + 1) else (i, j + 1))))
        return g_

    def bfs(g):
        seen = set()
        q = collections.deque([])
        q.append((0, 0, 1))

        while q:
            g = advance(g)

            k = len(q)

            for _ in range(k):
                t, i, j = q.popleft()
                if (i, j) == (m - 1, n - 2):
                    return t

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
                    i_ = i + di
                    j_ = j + dj

                    if 0 <= i_ < m and 0 <= j_ < n and not wall(i_, j_) and (t + 1, i_, j_) not in seen:
                        safe = True
                        for _, bi, bj in g:
                            if i_ == bi and j_ == bj:
                                safe = False
                                break
                        if safe:
                            seen.add((t + 1, i_, j_))
                            q.append((t + 1, i_, j_))

        return -1

    g = initialize()
    return bfs(g)

def main():
    with open("input/24.data") as f:
        grid = [list(line.strip()) for line in f.readlines()]
        print(solve(grid))

if __name__ == "__main__":
    main()
