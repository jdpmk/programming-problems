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

    seen = {}
    seen_again = {}

    for i in range(1000000000000):
        x, y = make_piece(t, max_y)
        max_y, ptr = move(stream, grid, x, y, t, max_y, ptr)

        # find a pattern which repeats itself (twice for good measure).
        # the key used is the type of block falling, the position in the jetstream,
        # and a bitshift-encoded representation of the topmost surface of the cave

        base = 0
        for x, y in grid:
            if y == max_y:
                base |= 1 << x

        if (t, ptr, base) in seen:
            if (t, ptr, base) in seen_again:
                print("Found repeated pattern for the second time at block", i, "of type", t, \
                      "at jetstream position", ptr, "with topmost cave surface", base, "at height", max_y)
                return
            seen_again[(t, ptr, base)] = i
            print("Found repeated pattern at block", i, "of type", t, "at jetstream position", \
                  ptr, "with topmost cave surface", base, "at height", max_y)
        seen[(t, ptr, base)] = i

        t = (t + 1) % NUM_PIECES

        """
        Examples:

        Sample:
            pattern start: 79 at block 50
            pattern end: 132 at block 85

            132 - 79 = +53 height difference every 85 - 50 = 35 blocks after 50

            (this approach can even be used to solve smaller samples with just
            2022 blocks, although, the simulation works as well)

            for 2022 total blocks:
                2022 - 50 = 1972 blocks left after initial height of 79 at block 50
                1972 // 35 = 56 repetitions of the pattern
                1972 % 35 = 12 remaining blocks not a part of a complete pattern
                height at 12th block of the pattern is 100 at block 61
                last blocks have a height difference of 100 - 79 = +21
                79 + 56 * 53 + 21 = [3068]

            for 1000000000000 total blocks:
                1e12 - 50 blocks left after initial height of 79 at block 50
                (1e12 - 50) // 35 = 28571428570 repetitions of the pattern
                (1e12 - 50) % 35 = 0 remaining blocks not a part of a complete pattern
                79 + 28571428570 * 53 = [1514285714289] (off by one?)

        My input:
            pattern start: 2980 at block 1875
            pattern end: 5765 at block 3620

            5765 - 2980 = +2785 height difference every 3620 - 1875 = 1745 blocks after 1875

            for 1000000000000 total blocks:
                1e12 - 1875 blocks left after initial height of 2980 at block 1875
                (1e12 - 1875) // 1745 = 573065901 repetitions of the pattern
                (1e12 - 1875) % 1745 = 880 remaining blocks not a part of a complete pattern
                height at 880th block of the pattern is 4406 at block 2754
                last blocks have a height difference of 4406 - 2980 = +1426
                2980 + 573065901 * 2785 + 1426 = [1595988538691]
        """

    return max_y

def main():
    with open("input/17.data") as f:
        stream = f.read().strip()
        print(solve(stream))

if __name__ == "__main__":
    main()
