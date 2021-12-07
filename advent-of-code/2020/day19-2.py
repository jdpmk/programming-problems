import re

def traverse(g, k, processed):
    if "\"" in g[k]:
        return g[k].strip("\"")
    if processed.get(k, False):
        if k == 8:
            g[k] = traverse(g, 42, processed) + "+"
        if k == 11:
            p1 = traverse(g, 42, processed)
            p2 = traverse(g, 31, processed)
            g[k] = (p1 + "(") * 5 + p1 + p2 + (")*" + p2) * 5
        return g[k]
    processed[k] = True
    options = []
    for seq in g[k]:
        results = []
        for adj in seq:
            results.append(traverse(g, adj, processed))
        options.append("".join([result.replace("^", "").replace("$", "") for result in results]))
    g[k] = "(" + "|".join(["^" + option + "$" for option in options]) + ")"
    return g[k]

def solve(rules, messages):
    g = {}
    for rule in rules:
        no, content = rule.split(": ")
        if no == "8":
            g[int(no)] = "42 | 42 8"
        elif no == "11":
            g[int(no)] = "42 31 | 42 11 31"
        else:
            g[int(no)] = content
    for k, v in g.items():
        if "\"" in v:
            continue
        g[k] = [[int(a) for a in seq.split(" ")] for seq in v.split(" | ")]

    processed = {}
    for k in g.keys():
        if not processed.get(k, False):
            traverse(g, k, processed)

    for k in g.keys():
        if "\"" not in g[k]:
            g[k] = g[k][1:len(g[k]) - 1]
        else:
            g[k] = "^" + g[k].strip("\"") + "$"

    matches = 0
    for message in messages:
        if re.match(g[0], message):
            matches += 1
    
    return matches

def main():
    with open("input/19.txt") as f:
        data = ""
        for line in f:
            data += line
        rules, messages = data.split("\n\n")
        print(solve(rules.split("\n"), messages.split("\n")))

if __name__ == "__main__":
    main()
