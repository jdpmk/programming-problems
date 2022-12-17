HORIZONTAL = 0
PLUS = 1
LSHAPE = 2
VERTICAL = 3
BLOCK = 4
NUM_PIECES = 5

SIDEWAYS = False
DOWNWARDS = True

LEFT = "<"
RIGHT = ">"

def make_piece(t, max_y):
    if t == HORIZONTAL:
        return 2, max_y + 4
    if t == PLUS:
        return 2, max_y + 4 + 2
    if t == LSHAPE:
        return 2, max_y + 4 + 2
    if t == VERTICAL:
        return 2, max_y + 4 + 3
    if t == BLOCK:
        return 2, max_y + 4 + 1

def move(stream, grid, x, y, t, max_y, ptr):
    direction = SIDEWAYS

    while True:
        if direction == SIDEWAYS:
            if stream[ptr] == LEFT and t == HORIZONTAL:
                if 0 <= x - 1 and (x - 1, y) not in grid:
                    x -= 1
            if stream[ptr] == LEFT and t == PLUS:
                if (x, y) not in grid and \
                   0 <= x - 1 and (x - 1, y - 1) not in grid and \
                   (x, y - 2) not in grid:
                       x -= 1
            if stream[ptr] == LEFT and t == LSHAPE:
                if (x + 1, y) not in grid and \
                   (x + 1, y + 1) not in grid and \
                   0 <= x - 1 and (x - 1, y - 2) not in grid:
                       x -= 1
            if stream[ptr] == LEFT and t == VERTICAL:
                if 0 <= x - 1 and (x - 1, y) not in grid and \
                   (x - 1, y - 1) not in grid and \
                   (x - 1, y - 2) not in grid and \
                   (x - 1, y - 3) not in grid:
                       x -= 1
            if stream[ptr] == LEFT and t == BLOCK:
                if 0 <= x - 1 and (x - 1, y) not in grid and \
                    (x - 1, y - 1) not in grid:
                        x -= 1
            if stream[ptr] == RIGHT and t == HORIZONTAL:
                if x + 4 <= 6 and (x + 4, y) not in grid:
                    x += 1
            if stream[ptr] == RIGHT and t == PLUS:
                if x + 2 <= 6 and (x + 2, y) not in grid and \
                   x + 3 <= 6 and (x + 3, y - 1) not in grid and \
                   (x + 2, y - 2) not in grid:
                       x += 1
            if stream[ptr] == RIGHT and t == LSHAPE:
                if x + 3 <= 6 and (x + 3, y) not in grid and \
                   (x + 3, y - 1) not in grid and \
                   (x + 3, y - 2) not in grid:
                       x += 1
            if stream[ptr] == RIGHT and t == VERTICAL:
                if x + 1 <= 6 and (x + 1, y) not in grid and \
                   (x + 1, y - 1) not in grid and \
                   (x + 1, y - 2) not in grid and \
                   (x + 1, y - 3) not in grid:
                       x += 1
            if stream[ptr] == RIGHT and t == BLOCK:
                if x + 2 <= 6 and (x + 2, y) not in grid and \
                   (x + 2, y - 1) not in grid:
                       x += 1
            ptr = (ptr + 1) % len(stream)
        elif direction == DOWNWARDS:
            if t == HORIZONTAL:
                if 0 < y - 1 and (x, y - 1) not in grid and \
                   (x + 1, y - 1) not in grid and \
                   (x + 2, y - 1) not in grid and \
                   (x + 3, y - 1) not in grid:
                       y -= 1
                else:
                    grid.add((x, y))
                    grid.add((x + 1, y))
                    grid.add((x + 2, y))
                    grid.add((x + 3, y))
                    max_y = max(max_y, y)
                    break
            if t == PLUS:
                if 0 < y - 2 and (x, y - 2) not in grid and \
                   0 < y - 3 and (x + 1, y - 3) not in grid and \
                   (x + 2, y - 2) not in grid:
                       y -= 1
                else:
                    grid.add((x + 1, y))
                    grid.add((x, y - 1))
                    grid.add((x + 1, y - 1))
                    grid.add((x + 2, y - 1))
                    grid.add((x + 1, y - 2))
                    max_y = max(max_y, y)
                    break
            if t == LSHAPE:
                if 0 < y - 3 and (x, y - 3) not in grid and \
                   (x + 1, y - 3) not in grid and \
                   (x + 2, y - 3) not in grid:
                       y -= 1
                else:
                    grid.add((x + 2, y))
                    grid.add((x + 2, y - 1))
                    grid.add((x + 2, y - 2))
                    grid.add((x, y - 2))
                    grid.add((x + 1, y - 2))
                    max_y = max(max_y, y)
                    break
            if t == VERTICAL:
                if 0 < y - 4 and (x, y - 4) not in grid:
                    y -= 1
                else:
                    grid.add((x, y))
                    grid.add((x, y - 1))
                    grid.add((x, y - 2))
                    grid.add((x, y - 3))
                    max_y = max(max_y, y)
                    break
            if t == BLOCK:
                if 0 < y - 2 and (x, y - 2) not in grid and \
                   (x + 1, y - 2) not in grid:
                       y -= 1
                else:
                    grid.add((x, y))
                    grid.add((x + 1, y))
                    grid.add((x, y - 1))
                    grid.add((x + 1, y - 1))
                    max_y = max(max_y, y)
                    break

        direction = not direction

    return max_y, ptr

def solve(stream):
    t = HORIZONTAL
    max_y = 0
    ptr = 0
    grid = set()

    for i in range(2022):
        x, y = make_piece(t, max_y)
        max_y, ptr = move(stream, grid, x, y, t, max_y, ptr)
        t = (t + 1) % NUM_PIECES

    return max_y

def main():
    with open("input/17.data") as f:
        stream = f.read().strip()
        print(solve(stream))

if __name__ == "__main__":
    main()
