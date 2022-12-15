import math

RANGE = 4000000

def transform_report(report):
    sensor, beacon = report.split(": ")
    sx, sy = sensor.split(", ")
    _, sx = sx.split("=")
    _, sy = sy.split("=")
    bx, by = beacon.split(", ")
    _, bx = bx.split("=")
    _, by = by.split("=")
    return (int(sx), int(sy)), (int(bx), int(by))

def manhattan(a, b, c, d):
    return abs(a - c) + abs(b - d)

def get_border(report):
    (sx, sy), (bx, by) = report
    dist = manhattan(sx, sy, bx, by)

    tx, ty = sx, sy - dist - 1
    bx, by = sx, sy + dist + 1
    lx, ly = sx - dist - 1, sy
    rx, ry = sx + dist + 1, sy

    border = []

    x, y = tx, ty
    while (x, y) != (rx, ry):
        border.append((x, y))
        x, y = x + 1, y + 1
    while (x, y) != (bx, by):
        border.append((x, y))
        x, y = x - 1, y + 1
    while (x, y) != (lx, ly):
        border.append((x, y))
        x, y = x - 1, y - 1
    while (x, y) != (tx, ty):
        border.append((x, y))
        x, y = x + 1, y - 1

    return border

def solve(reports):
    reports = list(map(transform_report, reports))

    for i, a in enumerate(reports):
        border = get_border(a)

        for x, y in border:
            intersects = False

            for j, b in enumerate(reports, i + 1):
                (sx, sy), (bx, by) = b
                dist = manhattan(sx, sy, bx, by)

                if manhattan(sx, sy, x, y) <= dist:
                    intersects = True
                    break

            if not intersects and 0 <= x <= RANGE and 0 <= y <= RANGE:
                return x * 4000000 + y

    return -1

def main():
    with open("input/15.data") as f:
        reports = [line.strip() for line in f.readlines()]
        print(solve(reports))

if __name__ == "__main__":
    main()
