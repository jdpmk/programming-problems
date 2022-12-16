"""
References:
- https://www.reddit.com/r/adventofcode/comments/zn6k1l/comment/j0i5b26
"""

import collections
import math

START = "AA"
TIME = 26

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
    nonzero = set()

    for i, (u, flow, vs) in enumerate(valves):
        vid[u] = i 
        idv[i] = u
        if u == START or flow:
            nonzero.add(i)

    p = {}
    g = {}

    for u, flow, vs in valves:
        p[vid[u]] = flow
        g[vid[u]] = [vid[v] for v in vs]

    dist = {i: {j: math.inf for j in range(n) if i != j} for i in range(n)}
    for u, vs in g.items():
        dist[u][u] = 0
        for v in vs:
            dist[u][v] = 1
    for s in range(n):
        for u in range(n):
            for v in range(n):
                dist[u][v] = min(dist[u][v], dist[u][s] + dist[s][v])

    def is_activated(activated, i):
        return activated & (1 << i)

    def set_activated(activated, i):
        return activated | (1 << i)

    def generate_paths():
        paths = {}
        q = collections.deque()
        q.append((vid[START], 0, TIME, 0))

        while q:
            u, f, t, activated = q.popleft()

            paths[activated] = max(paths.get(activated, 0), f)

            for v, d in dist[u].items():
                if v in nonzero and not is_activated(activated, v) and dist[u][v] < t:
                    q.append((v, f + (t - d - 1) * p[v], t - d - 1, set_activated(activated, v)))

        return paths

    paths = generate_paths()

    best = 0
    for activated1, f1 in paths.items():
        for activated2, f2 in paths.items():
            if not activated1 & activated2:
                best = max(best, f1 + f2)

    return best

def main():
    with open("input/16.data") as f:
        valves = [transform_input(line.strip()) for line in f.readlines()]
        print(solve(valves))

if __name__ == "__main__":
    main()
