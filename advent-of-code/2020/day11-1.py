"""
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

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
        Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

            If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                    Otherwise, the seat's state does not change.
                    Floor (.) never changes; seats don't move, and nobody sits on the floor.

                    After one round of these rules, every seat in the example layout becomes occupied:

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
                    After a second round, the seats with four or more occupied adjacent seats become empty again:

                    #.LL.L#.##
                    #LLLLLL.L#
                    L.L.L..L..
                    #LLL.LL.L#
                    #.LL.LL.LL
                    #.LLLL#.##
                    ..L.L.....
                    #LLLLLLLL#
                    #.LLLLLL.L
                    #.#LLLL.##
                    This process continues for three more rounds:

                    #.##.L#.##
                    #L###LL.L#
                    L.#.#..#..
                    #L##.##.L#
                    #.##.LL.LL
                    #.###L#.##
                    ..#.#.....
                    #L######L#
                    #.LL###L.L
                    #.#L###.##
                    #.#L.L#.##
                    #LLL#LL.L#
                    L.L.L..#..
                    #LLL.##.L#
                    #.LL.LL.LL
                    #.LL#L#.##
                    ..L.L.....
                    #L#LLLL#L#
                    #.LLLLLL.L
                    #.#L#L#.##
                    #.#L.L#.##
            #LLL#LL.L#
            L.#.L..#..
            #L##.##.L#
            #.#L.LL.LL
            #.#L#L#.##
            ..L.L.....
            #L#L##L#L#
            #.LLLLLL.L
            #.#L#L#.##
            At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

            Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?
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
                    if within_bounds(new_i, new_j, M, N):
                        if data[new_i][new_j] == '#':
                            num_occupied += 1
                if data[i][j] == 'L' and num_occupied == 0:
                    change = True
                    result[i][j] = '#'
                if data[i][j] == '#' and num_occupied >= 4:
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
