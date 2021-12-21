def simulate(p1, p2, s1=0, s2=0, turn=False, memo={}):
    if (p1, p2, s1, s2, turn) in memo:
        return memo[(p1, p2, s1, s2, turn)]

    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)

    wins = (0, 0)
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                if not turn:
                    result = simulate((p1 + (i + j + k) - 1) % 10 + 1, p2, s1 + (p1 + (i + j + k) - 1) % 10 + 1, s2, not turn, memo)
                else:
                    result = simulate(p1, (p2 + (i + j + k) - 1) % 10 + 1, s1, s2 + (p2 + (i + j + k) - 1) % 10 + 1, not turn, memo)
                wins = tuple(map(sum, zip(wins, result)))

    memo[(p1, p2, s1, s2, turn)] = wins
    return wins

def solve(p1, p2):
    return max(simulate(p1, p2))

def main():
    with open("input/21.data") as f:
        p1 = int(f.readline().split()[-1])
        p2 = int(f.readline().split()[-1])
        print(solve(p1, p2))

if __name__ == "__main__":
    main()
