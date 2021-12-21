def roll(die):
    return (die + 3, 3 * die + 3)

def solve(p1, p2):
    num_rolls = 0
    die = 1
    s1, s2 = 0, 0

    while True:
        die, rolled = roll(die)
        num_rolls += 3
        p1 = (p1 + rolled) % 10
        s1 = s1 + p1 + 1

        if s1 >= 1000:
            return num_rolls * s2

        die, rolled = roll(die)
        num_rolls += 3
        p2 = (p2 + rolled) % 10
        s2 = s2 + p2 + 1

        if s2 >= 1000:
            return num_rolls * s1

def main():
    with open("input/21.data") as f:
        p1 = int(f.readline().split()[-1]) - 1
        p2 = int(f.readline().split()[-1]) - 1
        print(solve(p1, p2))

if __name__ == "__main__":
    main()
