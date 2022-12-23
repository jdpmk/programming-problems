import math

def solve(scan):
    m, n = len(scan), len(scan[0])

    def ok(state, r, c):
        return (r, c) not in state

    occ = set()
    for i in range(m):
        for j in range(n):
            if scan[i][j] == "#":
                occ.add((i, j))

    dirp = 0
    for _ in range(10):
        att = {}
        dst = {}
        next_occ = set()

        for r, c in occ:
            if all((r + dr, c + dc) not in occ for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), \
                                                              (0, 1), (1, -1,), (1, 0), (1, 1)]):
                continue

            for i in range(4):
                d = (dirp + i) % 4
                if d == 0 and ok(occ, r - 1, c - 1) and ok(occ, r - 1, c) and ok(occ, r - 1, c + 1):
                    att[(r - 1, c)] = att.get((r - 1, c), 0) + 1
                    dst[(r, c)] = (r - 1, c)
                    break
                elif d == 1 and ok(occ, r + 1, c - 1) and ok(occ, r + 1, c) and ok(occ, r + 1, c + 1):
                    att[(r + 1, c)] = att.get((r + 1, c), 0) + 1
                    dst[(r, c)] = (r + 1, c)
                    break
                elif d == 2 and ok(occ, r - 1, c - 1) and ok(occ, r, c - 1) and ok(occ, r + 1, c - 1):
                    att[(r, c - 1)] = att.get((r, c - 1), 0) + 1
                    dst[(r, c)] = (r, c - 1)
                    break
                elif d == 3 and ok(occ, r - 1, c + 1) and ok(occ, r, c + 1) and ok(occ, r + 1, c + 1):
                    att[(r, c + 1)] = att.get((r, c + 1), 0) + 1
                    dst[(r, c)] = (r, c + 1)
                    break

        for r, c in occ:
            if (r, c) not in dst or att[dst[(r, c)]] >= 2:
                next_occ.add((r, c))
            else:
                assert att[dst[(r, c)]] == 1
                next_occ.add(dst[(r, c)])

        assert len(next_occ) == len(occ)
        occ = next_occ.copy()
        dirp = (dirp + 1) % 4

        min_r, max_r = math.inf, -math.inf
        min_c, max_c = math.inf, -math.inf

        for r, c in occ:
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)

    min_r, max_r = math.inf, -math.inf
    min_c, max_c = math.inf, -math.inf

    for r, c in occ:
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)

    return (max_r - min_r + 1) * (max_c - min_c + 1) - len(occ)

def main():
    with open("input/23.data") as f:
        scan = [list(line.strip()) for line in f.readlines()]
        print(solve(scan))

if __name__ == "__main__":
    main()
