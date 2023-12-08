from functools import cmp_to_key

def rank(c):
    return 'J23456789TQKA'.index(c)

def kind(hand):
    ct = {}
    for c in hand:
        ct[c] = ct.get(c, 0) + 1

    jokers = ct.get("J", 0)

    vs = list(ct.values())
    if len(vs) == 1:
        kind = 6
    elif len(vs) == 2 and max(vs) == 4:
        kind = 5
    elif len(vs) == 2:
        kind = 4
    elif len(vs) == 3 and max(vs) == 3:
        kind = 3
    elif len(vs) == 3:
        kind = 2
    elif len(vs) == 4:
        kind = 1
    else:
        kind = 0

    if jokers > 0:
        if kind == 6: # JJJJJ
            return 6
        elif kind == 5: # JXXXX or XJJJJ
            return 6
        elif kind == 4: # JJXXX or XXXJJ
            return 6
        elif kind == 3: # JJJXY or XXXYJ
            return 5
        elif kind == 2:
            if ct["J"] == 2: # JJXXY
                return 5
            else: # XXYYJ
                return 4
        elif kind == 1: # JJXYZ
            return 3
        if kind == 0: # JWXYZ
            return 1

    return kind

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
