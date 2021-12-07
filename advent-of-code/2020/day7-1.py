import collections

def solve(data):
    g = {}
    for line in data:
        line = line[:-2]
        parent, children = line.split(" contain ")
        parent = " ".join(parent.split(" ")[:2])
        for child in children.split(", "):
            comp = child.split(" ")
            if len(comp) == 3:
                continue
            val = int(comp[0])
            child = " ".join(child.split(" ")[1:3])
            adj = g.get(child, [])
            adj.append(parent)
            g[child] = adj
    
    seen = set()
    q = collections.deque(["shiny gold"])
    while q:
        curr = q.popleft()
        if curr in seen:
            continue
        seen.add(curr)
        for neighbor in g.get(curr, []):
            q.append(neighbor)

    return len(seen) - 1

def main():
    with open("input/7.txt") as f:
        data = []
        for line in f:
            data.append(line)
        print(solve(data))

if __name__ == "__main__":
    main()
