ROCK = 0
SAND = 1
HOLE_X = 500
HOLE_Y = 0

def try_move_down(cave, x, y):
    assert cave[(x, y)] == SAND
    
    if (x, y + 1) in cave:
        return x, y, False

    del cave[(x, y)]
    cave[(x, y + 1)] = SAND
    return x, y + 1, True

def try_move_down_left(cave, x, y):
    assert cave[(x, y)] == SAND
    
    if (x - 1, y + 1) in cave:
        return x, y, False

    del cave[(x, y)]
    cave[(x - 1, y + 1)] = SAND
    return x - 1, y + 1, True

def try_move_down_right(cave, x, y):
    assert cave[(x, y)] == SAND
    
    if (x + 1, y + 1) in cave:
        return x, y, False

    del cave[(x, y)]
    cave[(x + 1, y + 1)] = SAND
    return x + 1, y + 1, True

def solve(rocks):
    cave = {}

    min_x = 1000
    min_y = 1000
    max_x = -1000
    max_y = -1000
    
    for rock in rocks:
        for x, y in rock:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    for rock in rocks:
        for i in range(len(rock) - 1):
            (sx, sy), (dx, dy) = rock[i], rock[i + 1]
            if sx == dx:
                for j in range(min(sy, dy), max(sy, dy) + 1):
                    cave[(sx, j)] = ROCK
            elif sy == dy:
                for j in range(min(sx, dx), max(sx, dx) + 1):
                    cave[(j, sy)] = ROCK

    num_placed = 0

    while True:
        x, y = HOLE_X, HOLE_Y
        cave[(x, y)] = SAND
        placed = False

        while not placed:
            if y > max_y:
                return num_placed

            x, y, ok = try_move_down(cave, x, y)
            if ok: continue
            x, y, ok = try_move_down_left(cave, x, y)
            if ok: continue
            x, y, ok = try_move_down_right(cave, x, y)
            if ok: continue

            placed = True
            num_placed += 1

    return -1

def main():
    with open("input/14.data") as f:
        rocks = [list(map(lambda coord: tuple(map(int, coord.split(","))), \
                          line.strip().split(" -> "))) for line in f.readlines()]
        print(solve(rocks))

if __name__ == "__main__":
    main()
