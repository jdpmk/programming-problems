def too_far(h, t):
    hr, hc = h
    tr, tc = t
    rd = abs(hr - tr)
    cd = abs(hc - tc)

    should_jump = max(rd, cd) >= 2
    next_pos = None

    if should_jump:
        if rd >= 2 and cd >= 2:
            next_pos = [(hr + tr) // 2, (hc + tc) // 2]
        elif rd >= 2:
            next_pos = [(hr + tr) // 2, hc]
        else:
            next_pos = [hr, (hc + tc) // 2]

    return should_jump, next_pos

def solve(steps):
    pos = [[0, 0] for _ in range(10)]
    lpos = [[0, 0] for _ in range(10)]

    visited = set()
    visited.add((0, 0))

    for step in steps:
        direction, magnitude = step.split()
        magnitude = int(magnitude)

        for s in range(magnitude):
            if direction == "U":
                lpos[0] = pos[0][:]
                pos[0][0] += 1
            elif direction == "D":
                lpos[0] = pos[0][:]
                pos[0][0] -= 1
            elif direction == "L":
                lpos[0] = pos[0][:]
                pos[0][1] -= 1
            else:
                lpos[0] = pos[0][:]
                pos[0][1] += 1

            for knot in range(1, 10):
                prev_knot = knot - 1
                should_jump, next_pos = too_far(pos[prev_knot], pos[knot])
                if should_jump:
                    lpos[knot] = pos[knot][:]
                    pos[knot] = next_pos
                    if knot == 9:
                        visited.add(tuple(pos[knot]))

    return len(visited)

def main():
    with open("input/9.data") as f:
        steps = [line.strip() for line in f.readlines()]
        print(solve(steps))

if __name__ == "__main__":
    main()
