def get_visited(path, steps_to):
    vis = set()
    x, y = 0, 0
    num_steps = 0

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

            num_steps += 1
            steps_to[(x, y)] = num_steps

    return vis

def solve(a, b):
    a_steps_to = {}
    b_steps_to = {}
    a_vis = get_visited(a, a_steps_to)
    b_vis = get_visited(b, b_steps_to)

    get_total_steps = lambda p: a_steps_to[p] + b_steps_to[p]
    return min(map(get_total_steps, a_vis & b_vis))

with open("input/3.data") as f:
    a, b = [line.strip().split(",") for line in f.readlines()]
    print(solve(a, b))
