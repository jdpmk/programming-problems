START = "AA"
TIME = 30

def transform_input(line):
    u, vs = line.split("; ")
    _, flow = u.split("=")
    u = u.split(" ")[1]
    try: _, vs = vs.split("valves ")
    except: _, vs = vs.split("valve ")
    vs = vs.split(", ")

    return u, int(flow), vs

def solve(valves):
    n = len(valves)

    vid = {}
    idv = {}

    for i, (u, _, _) in enumerate(valves):
        vid[u] = i
        idv[i] = u

    p = {}
    g = {}

    for u, flow, vs in valves:
        p[vid[u]] = flow
        g[vid[u]] = [vid[v] for v in vs]

    def is_activated(activated, i):
        return activated & (1 << i)

    def set_activated(activated, i):
        return activated | (1 << i)

    def all_activated(activated):
        return activated == (1 << (n + 1)) - 1

    def pressure(activated):
        total_pressure = 0
        for i in range(n):
            if is_activated(activated, i):
                total_pressure += p[i]
        return total_pressure

    def max_pressure(u, activated, t, seen):
        if t == 0:
            return 0

        if (u, activated, t) in seen:
            return seen[(u, activated, t)]

        released = pressure(activated)
        best = released

        if p[u] != 0 and not is_activated(activated, u):
            activated_ = set_activated(activated, u)
            flip = max_pressure(u, activated_, t - 1, seen)
            best = max(best, released + flip)

        for v in g[u]:
            move = max_pressure(v, activated, t - 1, seen)
            best = max(best, released + move)

        seen[(u, activated, t)] = best
        return best

    return max_pressure(vid[START], 0, TIME, {})

def main():
    with open("input/16.data") as f:
        valves = [transform_input(line.strip()) for line in f.readlines()]
        print(solve(valves))

if __name__ == "__main__":
    main()
