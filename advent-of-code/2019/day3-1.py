def get_visited(path):
    vis = set()
    x, y = 0, 0

    for step in path:
        d = step[0]
        m = int(step[1:])

        for i in range(m):
            if   d == "R": x += 1
            elif d == "L": x -= 1
            elif d == "U": y += 1
            elif d == "D": y -= 1
            else: assert False, d

            vis.add((x, y))

    return vis

def solve(a, b):
    a_vis = get_visited(a)
    b_vis = get_visited(b)

    manhattan = lambda p: abs(p[0]) + abs(p[1])
    return min(map(manhattan, a_vis & b_vis))

with open("input/3.data") as f:
    a, b = [line.strip().split(",") for line in f.readlines()]
    print(solve(a, b))
