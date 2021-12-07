import copy

CYCLES = 6

def solve(data):
    minh, maxh = -1, len(data) + 1
    minw, maxw = -1, len(data[0]) + 1
    mind, maxd = -1, 1 + 1

    cubes = {}
    for i in range(minh, maxh + 1):
        for j in range(minw, maxw + 1):
            for k in range(mind, maxd + 1):
                cubes[(i, j, k)] = data[i][j] if i in range(0, len(data)) and j in range(0, len(data[0])) and k == 0 else "."

    for cycle in range(CYCLES):
        cp = copy.deepcopy(cubes)
        for i in range(minh - 1, maxh + 2):
            for j in range(minw - 1, maxw + 2):
                for k in range(mind - 1, maxd + 2):
                    changed = False
                    active_count = 0
                    for a in [-1, 0, 1]:
                        for b in [-1, 0, 1]:
                            for c in [-1, 0, 1]:
                                if a == 0 and b == 0 and c == 0:
                                    continue
                                i_, j_, k_ = i + a, j + b, k + c
                                if (i_, j_, k_) in cubes and cubes[(i_, j_, k_)] == "#":
                                    active_count += 1
                    if cubes.get((i, j, k), ".") == "." and active_count == 3:
                        cp[(i, j, k)] = "#"
                        changed = True
                    elif cubes.get((i, j, k), ".") == "#" and active_count not in [2, 3]:
                        cp[(i, j, k)] = "."
                        changed = True
                    if changed:
                        minh = min(minh, i)
                        maxh = max(maxh, i)
                        minw = min(minw, j)
                        maxw = max(maxw, j)
                        mind = min(mind, k)
                        maxd = max(maxd, k)
        cubes = copy.deepcopy(cp)
    
    num_active = 0
    for i in range(minh - 1, maxh + 1):
        for j in range(minw - 1, maxw + 1):
            for k in range(mind - 1, maxd + 1):
                if cubes.get((i, j, k), ".") == "#":
                    num_active += 1
    return num_active

def main():
    with open("input/17.txt") as f:
        data = []
        for line in f:
            data.append(list(line.strip()))
        print(solve(data))

if __name__ == "__main__":
    main()
