within = lambda r, l, u: -r <= l <= u <= r

def toggle(reactor, flip, xr, yr, zr):
    for i in xr:
        reactor[i] = reactor.get(i, {})
        for j in yr:
            reactor[i][j] = reactor[i].get(j, {})
            for k in zr:
                reactor[i][j][k] = flip == "on"

    return reactor

def solve(steps):
    reactor = {}

    for i, (flip, cuboid) in enumerate(steps):
        xd, yd, zd = cuboid.split(",")
        _, xr = xd.split("=")
        xlb, xub = map(int, xr.split(".."))
        _, yr = yd.split("=")
        ylb, yub = map(int, yr.split(".."))
        _, zr = zd.split("=")
        zlb, zub = map(int, zr.split(".."))

        if within(50, xlb, xub) and within(50, ylb, yub) and within(50, zlb, zub):
            toggle(reactor, flip, range(xlb, xub + 1), range(ylb, yub + 1), range(zlb, zub + 1))

    ct = 0
    for i in range(-50, 51):
        reactor[i] = reactor.get(i, {})
        for j in range(-50, 51):
            reactor[i][j] = reactor[i].get(j, {})
            for k in range(-50, 51):
                ct += reactor[i][j].get(k, False)

    return ct

def main():
    with open("input/22.data") as f:
        steps = [line.strip().split() for line in f.readlines()]
        print(solve(steps))

if __name__ == "__main__":
    main()
