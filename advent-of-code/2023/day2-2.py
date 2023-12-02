import math

def parse(s):
    game = []
    _, s = s.split(": ")
    for rs in s.split("; "):
        r = []
        cs = rs.split(", ")
        for xs in cs:
            r.append((lambda x: (int(x[0]), x[1]))(xs.split()))
        game.append(r)
    return game

def solve(games):
    total = 0

    for i, g in enumerate(games):
        req = {}
        for (n, c) in (x for r in g for x in r):
            req[c] = max(req.get(c, 0), n)
        total += math.prod(req.values())

    return total

def main():
    with open("input/2.data") as f:
        games = [parse(game.strip()) for game in f.readlines()]
        print(solve(games))

if __name__ == "__main__":
    main()
