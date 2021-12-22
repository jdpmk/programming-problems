def overlaps(l1, u1, l2, u2):
    return not (l1 <= u1 <= l2 <= u2 or l2 <= u2 <= l1 <= u1)

def merge(cuboids, flip, xlb, xub, ylb, yub, zlb, zub):
    to_add = []
    for i, (toggle, (x1, x2), (y1, y2), (z1, z2)) in enumerate(cuboids):
        if overlaps(x1, x2, xlb, xub) and overlaps(y1, y2, ylb, yub) and overlaps(z1, z2, zlb, zub):
            # since an overlap is guaranteed, the overlapping interval is
            # the maximum of the lower bounds and minimum of the upper bounds
            ox1 = max(x1, xlb)
            ox2 = min(x2, xub)
            oy1 = max(y1, ylb)
            oy2 = min(y2, yub)
            oz1 = max(z1, zlb)
            oz2 = min(z2, zub)

            # if the existing cuboid is on, turn this overlap off to avoid duplicates
            # if the existing cuboid is off, turn this overlap on to "neutralize" the space
            to_add.append((not toggle, (ox1, ox2), (oy1, oy2), (oz1, oz2)))

    flip == "on" and cuboids.append((True, (xlb, xub), (ylb, yub), (zlb, zub)))
    cuboids.extend(to_add)

def solve(steps):
    cuboids = []

    for i, (flip, cuboid) in enumerate(steps):
        xd, yd, zd = cuboid.split(",")
        _, xr = xd.split("=")
        xlb, xub = map(int, xr.split(".."))
        _, yr = yd.split("=")
        ylb, yub = map(int, yr.split(".."))
        _, zr = zd.split("=")
        zlb, zub = map(int, zr.split(".."))

        merge(cuboids, flip, xlb, xub, ylb, yub, zlb, zub)

    ct = 0
    for toggle, (x1, x2), (y1, y2), (z1, z2) in cuboids:
        assert x2 >= x1 and y2 >= y1 and z2 >= z1
        ct += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * (1 if toggle else -1)

    return ct

def main():
    with open("input/22.data") as f:
        steps = [line.strip().split() for line in f.readlines()]
        print(solve(steps))

if __name__ == "__main__":
    main()
