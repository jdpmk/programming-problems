from functools import cmp_to_key

def rank(c):
    return '23456789TJQKA'.index(c)

def kind(hand):
    ct = {}
    for c in hand:
        ct[c] = ct.get(c, 0) + 1

    vs = list(ct.values())
    if len(vs) == 1:
        return 6
    if len(vs) == 2 and max(vs) == 4:
        return 5
    if len(vs) == 2:
        return 4
    if len(vs) == 3 and max(vs) == 3:
        return 3
    if len(vs) == 3:
        return 2
    if len(vs) == 4:
        return 1
    return 0

def cmp(a, b):
    a = a[0]
    b = b[0]

    ka = kind(a)
    kb = kind(b)

    if ka < kb: return -1
    if ka > kb: return 1

    i = 0
    while i < 5:
        ra = rank(a[i])
        rb = rank(b[i])
        if ra < rb:
            return -1
        if ra > rb:
            return 1
        i += 1

    assert False

def solve(pairs):
    hands = [(p[0], i) for i, p in enumerate(pairs)]
    hands.sort(key=cmp_to_key(cmp))

    total = 0
    for i, (hand, j) in enumerate(hands):
        total += pairs[j][1] * (i + 1)

    return total

def main():
    with open("input/7.data") as f:
        pairs = map(lambda x: (x[0], int(x[1])),
                    [line.strip().split() for line in f.readlines()])
        print(solve(list(pairs)))

if __name__ == "__main__":
    main()
