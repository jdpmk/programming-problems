def solve(xs):
    n = len(xs)

    order = xs[:]
    xs = [(x, i) for i, x in enumerate(xs)]

    for i, x in enumerate(order):
        if x == 0:
            continue

        idx = xs.index((x, i))
        di = x // abs(x)

        src = idx
        dst = (idx + abs(x) * di) % (n - 1)

        xs.insert(dst, xs.pop(src))

    zero_idx = next(i for i, (x, _) in enumerate(xs) if x == 0)
    return sum(xs[(zero_idx + offset) % n][0] for offset in [1000, 2000, 3000])

def main():
    with open("input/20.data") as f:
        xs = [int(line.strip()) for line in  f.readlines()]
        print(solve(xs))

if __name__ == "__main__":
    main()
