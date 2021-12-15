def dfs(G, v, visited, lower, upper):
    if v == "end":
        return 1

    visited[v] = True

    num_paths = 0
    for u in G[v]:
        if not visited.get(u, False) or u in upper:
            num_paths += dfs(G, u, visited, lower, upper)

    visited[v] = False

    return num_paths

def solve(E):
    G = {}
    upper = set()
    lower = set()

    for u, v in E:
        G[u] = G.get(u, []) + [v]
        G[v] = G.get(v, []) + [u]

        if u not in ["start", "end"]:
            if u.islower(): lower.add(u)
            else: upper.add(u)

        if v not in ["start", "end"]:
            if v.islower(): lower.add(v)
            else: upper.add(v)

    return dfs(G, "start", {}, lower, upper)

def main():
    with open("input/12.data") as f:
        E = [line.strip().split("-") for line in f.readlines()]
        print(solve(E))

if __name__ == "__main__":
    main()
