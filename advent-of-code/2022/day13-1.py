WRONG = 0
RIGHT = 1
CONT  = 2

def ordered(a, b):
    if type(a) == type(b) == int:
        if a < b: return RIGHT
        elif a == b: return CONT
        else: return WRONG

    if type(a) == type(b) == list:
        if not a and b: return RIGHT
        if not b and a: return WRONG
        if not a and not b: return CONT

        first = ordered(a[0], b[0])
        if first == WRONG: return WRONG
        if first == RIGHT: return RIGHT

        return ordered(a[1:], b[1:])

    if type(a) == int: a = [a]
    if type(b) == int: b = [b]
    return ordered(a, b)

def solve(pairs):
    total = 0

    for i, pair in enumerate(pairs):
        if ordered(*pair):
            total += i + 1

    return total

def main():
    with open("input/13.data") as f:
        contents = "\n".join(line.strip() for line in f.readlines())
        pairs = []
        for pair in contents.split("\n\n"):
            a, b = pair.split("\n")
            pairs.append((eval(a), eval(b)))

        print(solve(pairs))

if __name__ == "__main__":
    main()
