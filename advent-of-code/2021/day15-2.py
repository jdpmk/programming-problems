import heapq

def solve(cavern):
    m, n = len(cavern), len(cavern[0])

    visited = set()
    pq = []

    visited.add((0, 0))
    heapq.heappush(pq, (0, (0, 0)))

    while pq:
        risk, (i, j) = heapq.heappop(pq)

        if (i, j) == (m * 5 - 1, n * 5 - 1):
            return risk

        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if di or dj:
                i_ = i + di
                j_ = j + dj
                if 0 <= i_ < m * 5 and 0 <= j_ < n * 5:
                    if (i_, j_) not in visited:
                        visited.add((i_, j_))
                        heapq.heappush(pq, (risk + (cavern[i_ % m][j_ % n] - 1 + i_ // m + j_ // n) % 9 + 1, (i_, j_)))

    assert False

def main():
    with open("input/15.data") as f:
        cavern = [[int(x) for x in line.strip()] for line in f.readlines()]
        print(solve(cavern))

if __name__ == "__main__":
    main()
