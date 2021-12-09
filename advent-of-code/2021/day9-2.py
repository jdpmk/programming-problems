dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(heightmap, visited, i, j, m, n):
    visited[i][j] = True

    basin_size = 1
    for di, dj in dirs:
        i_ = i + di
        j_ = j + dj

        if 0 <= i_ < m and 0 <= j_ < n:
            if heightmap[i][j] < heightmap[i_][j_] and heightmap[i_][j_] != 9 and not visited[i_][j_]:
                basin_size += dfs(heightmap, visited, i + di, j + dj, m, n)

    return basin_size

def solve(heightmap):
    m, n = len(heightmap), len(heightmap[0])
    visited = [[False for _ in range(n)] for _ in range(m)]

    points = {}
    for i in range(m):
        for j in range(n):
            points[heightmap[i][j]] = points.get(heightmap[i][j], []) + [(i, j)]

    basins = []
    for height in range(len(points)):
        for i, j in points.get(height, []):
            if not visited[i][j]:
                basins.append(dfs(heightmap, visited, i, j, m, n))

    a, b, c = sorted(basins, reverse=True)[:3]
    return a * b * c

def main():
    with open("input/9.data") as f:
        heightmap = [[int(x) for x in line.strip()] for line in f.readlines()]
        print(solve(heightmap))

if __name__ == "__main__":
    main()
