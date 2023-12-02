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
    limit = {"red": 12, "green": 13, "blue": 14}
    total = 0

    for i, g in enumerate(games):
        possible = True
        for (n, c) in (x for r in g for x in r):
            if n > limit[c]:
                possible = False
                break

        if possible:
            total += i + 1

    return total

def main():
    with open("input/2.data") as f:
        games = [parse(game.strip()) for game in f.readlines()]
        print(solve(games))

if __name__ == "__main__":
    main()
