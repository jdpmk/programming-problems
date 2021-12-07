import copy

DIRS = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -2), (0, 2)]

def move(instruction, i, j):
    if instruction == "nw":
        return i - 1, j - 1
    if instruction == "ne":
        return i - 1, j + 1
    if instruction == "sw":
        return i + 1, j - 1
    if instruction == "se":
        return i + 1, j + 1
    if instruction == "w":
        return i, j - 2
    if instruction == "e":
        return i, j + 2
    assert False

def solve(tiles):
    state = {}
    for tile in tiles:
        i, j = 0, 0
        x = 0
        while x < len(tile):
            offset = 2 if tile[x] in "ns" else 1
            instruction = tile[x:x+offset]
            x += offset
            i, j = move(instruction, i, j)
            assert i % 2 == j % 2
        state[(i, j)] = not state.get((i, j), True)

    for d in range(100):
        cp = copy.deepcopy(state)
        for i in range(-200, 200):
            for j in range(-200, 200):
                if i % 2 != j % 2:
                    continue
                curr_color = state.get((i, j), True)
                count_black = 0
                for dy, dx in DIRS:
                    r, s = i + dy, j + dx
                    if not state.get((r, s), True):
                        count_black += 1
                if not curr_color:
                    if count_black == 0 or count_black > 2:
                        cp[(i, j)] = True
                else:
                    if count_black == 2:
                        cp[(i, j)] = False
        state = copy.deepcopy(cp)
        count = 0
        for k, v in state.items():
            if not v:
                count += 1

    return count

def main():
    with open("input/24.txt") as f:
        data = []
        for line in f:
            data.append(line)
        print(solve([tile.strip() for tile in data]))

if __name__ == "__main__":
    main()
