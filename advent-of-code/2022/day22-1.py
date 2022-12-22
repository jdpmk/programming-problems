BLANK = " "
OPEN = "."
WALL = "#"

DIR = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def parse_steps(steps_str):
    steps = []
    read_num = True

    while steps_str:
        if read_num:
            broke = False
            for i in range(len(steps_str)):
                if not steps_str[i].isdigit():
                    steps.append(int(steps_str[:i]))
                    broke = True
                    break
            if not broke:
                steps.append(int(steps_str))
                break
            steps_str = steps_str[i:]
        else:
            steps.append(steps_str[0])
            steps_str = steps_str[1:]
        read_num = not read_num

    return steps

def good_wraparound(seq, s, e):
    for i in range(s, e):
        if seq[i] == WALL:
            return False, -1
        elif seq[i] == OPEN:
            return True, i
        else: # BLANK
            continue

    assert False

def solve(board, steps):
    steps = parse_steps(steps)

    board = board.split("\n")
    m, n = len(board), len(board[0])
    r, c = 0, board[0].index(OPEN)
    dirp = 0

    for step in steps:
        if type(step) == int:
            for i in range(step):
                dr, dc = DIR[dirp]
                r_ = r + dr
                c_ = c + dc

                if not (0 <= r_ < m and 0 <= c_ < n) or board[r_][c_] == BLANK:
                    if dirp == 0:
                        r__, (ok, c__) = r_, good_wraparound(board[r], 0, n)
                        if not ok: break
                        r, c = r__, c__
                    elif dirp == 1:
                        (ok, r__), c__ = good_wraparound([x for j in range(m) for x in board[j][c]], 0, m), c_
                        if not ok: break
                        r, c = r__, c__
                    elif dirp == 2:
                        r__, (ok, c__) = r_, good_wraparound(list(reversed(board[r])), 0, n)
                        if not ok: break
                        r, c = r__, n - 1 - c__
                    elif dirp == 3:
                        (ok, r__), c__ = good_wraparound(list(reversed([x for j in range(m) for x in board[j][c]])), 0, m), c_
                        if not ok: break
                        r, c = m - 1 - r__, c__
                else:
                    if board[r_][c_] == WALL:
                        break
                    r, c = r_, c_
        else:
            if step == "R": dirp = (dirp + 1) % 4
            elif step == "L":  dirp = (dirp - 1) % 4
            else: assert False

    return 1000 * (r + 1) + 4 * (c + 1) + dirp

def main():
    with open("input/22.data") as f:
        lines = "\n".join([line[:-1] for line in f.readlines()])
        board, steps = lines.split("\n\n")
        print(solve(board, steps))

if __name__ == "__main__":
    main()
