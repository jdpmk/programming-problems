"""
--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

    .......#.
    ...#.....
    .#.......
    .........
    ..#L....#
    ....#....
    .........
    #........
    ...#.....
    The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

        .............
        .L.L.#.#.#.#.
        .............
        The empty seat below would see no occupied seats:

            .##.##.
            #.#.#.#
            ##...##
            ...L...
            ##...##
            #.#.#.#
            .##.##.
            Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

            Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

            L.LL.LL.LL
            LLLLLLL.LL
            L.L.L..L..
            LLLL.LL.LL
            L.LL.LL.LL
            L.LLLLL.LL
            ..L.L.....
            LLLLLLLLLL
            L.LLLLLL.L
            L.LLLLL.LL
            #.##.##.##
            #######.##
            #.#.#..#..
            ####.##.##
            #.##.##.##
            #.#####.##
            ..#.#.....
            ##########
            #.######.#
            #.#####.##
            #.LL.LL.L#
            #LLLLLL.LL
            L.L.L..L..
            LLLL.LL.LL
            L.LL.LL.LL
            L.LLLLL.LL
            ..L.L.....
            LLLLLLLLL#
            #.LLLLLL.L
            #.LLLLL.L#
            #.L#.##.L#
            #L#####.LL
            L.#.#..#..
            ##L#.##.##
            #.##.#L.##
            #.#####.#L
            ..#.#.....
            LLL####LL#
            #.L#####.L
            #.L####.L#
            #.L#.L#.L#
            #LLLLLL.LL
            L.L.L..#..
            ##LL.LL.L#
            L.LL.LL.L#
            #.LLLLL.LL
            ..L.L.....
            LLLLLLLLL#
            #.LLLLL#.L
            #.L#LL#.L#
            #.L#.L#.L#
            #LLLLLL.LL
            L.L.L..#..
            ##L#.#L.L#
            L.L#.#L.L#
            #.L####.LL
            ..#.#.....
            LLL###LLL#
            #.LLLLL#.L
            #.L#LL#.L#
            #.L#.L#.L#
            #LLLLLL.LL
            L.L.L..#..
            ##L#.#L.L#
            L.L#.LL.L#
            #.LLLL#.LL
            ..#.L.....
            LLL###LLL#
            #.LLLLL#.L
            #.L#LL#.L#
            Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

            Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?
"""

def within_bounds(i, j, M, N):
    return not(i < 0 or i > M - 1 or j < 0 or j > N - 1)

def solve(data):
    M, N = len(data), len(data[0])
    result = [[data[i][j] for j in range(N)] for i in range(M)]
    DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    change = True
    while change:
        change = False
        for i in range(M):
            for j in range(N):
                num_occupied = 0
                for direction in DIRS:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    while within_bounds(new_i, new_j, M, N) and data[new_i][new_j] == '.':
                        new_i += direction[0]
                        new_j += direction[1]
                    if within_bounds(new_i, new_j, M, N):
                        if data[new_i][new_j] == '#':
                            num_occupied += 1
                if data[i][j] == 'L' and num_occupied == 0:
                    change = True
                    result[i][j] = '#'
                if data[i][j] == '#' and num_occupied >= 5:
                    change = True
                    result[i][j] = 'L'
        data = [[result[i][j] for j in range(N)] for i in range(M)]

    occupied_steady_state = 0
    for i in range(M):
        for j in range(N):
            if result[i][j] == '#':
                occupied_steady_state += 1
    return occupied_steady_state

def main():
    with open("input/11.txt") as f:
        data = []
        for line in f:
            data.append(line.strip())
        print(solve(data))

if __name__ == "__main__":
    main()
