import collections

def dfs(g, n):
    total = 0
    for child in g.get(n, []):
        total += child[0] + child[0] * dfs(g, child[1])
    return total

def solve(data):
    g = {}
    for line in data:
        line = line[:-2]
        parent, children = line.split(" contain ")
        parent = " ".join(parent.split(" ")[:2])
        adj = g.get(parent, [])
        for child in children.split(", "):
            comp = child.split(" ")
            if len(comp) == 3:
                continue
            val = int(comp[0])
            child = " ".join(child.split(" ")[1:3])
            adj.append((val, child))
        g[parent] = adj
    
    return dfs(g, "shiny gold")

def main():
    with open("input/7.txt") as f:
        data = []
        for line in f:
            data.append(line)
        print(solve(data))

if __name__ == "__main__":
    main()
