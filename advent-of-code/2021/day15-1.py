"""
Dynamic programming - evaluate graph in reverse topological order

*Technically* this isn't supposed to work, since the graph is not
acyclic... but it does? ¯\_(ツ)_/¯

See `day15-2.py` for an implementation of Dijkstra's.
"""

def solve(cavern):
    m, n = len(cavern), len(cavern[0])

    min_risk = [[0 for _ in range(n)] for _ in range(m)]
    min_risk[0][0] = cavern[0][0]

    for i in range(1, m):
        min_risk[i][0] = min_risk[i - 1][0] + cavern[i][0]
    for i in range(1, n):
        min_risk[0][i] = min_risk[0][i - 1] + cavern[0][i]

    for i in range(1, m):
        for j in range(1, n):
            min_risk[i][j] = cavern[i][j] + min(min_risk[i - 1][j], min_risk[i][j - 1])

    return min_risk[-1][-1] - cavern[0][0]

def main():
    with open("input/15.data") as f:
        cavern = [[int(x) for x in line.strip()] for line in f.readlines()]
        print(solve(cavern))

if __name__ == "__main__":
    main()
