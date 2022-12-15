import math

TARGET = 2000000

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

def solve(reports):
    reports = list(map(lambda report: transform_report(report), reports))

    min_x = math.inf
    min_y = math.inf
    max_x = -math.inf
    max_y = -math.inf
    sensors = set()
    beacons = set()
    impossible = set()

    for (sx, sy), (bx, by) in reports:
        min_x = min(min_x, sx, bx)
        min_y = min(min_y, sy, by)
        max_x = max(max_x, sx, bx)
        max_y = max(max_y, sy, by)
        sensors.add((sx, sy))
        beacons.add((bx, by))

    for i, ((sx, sy), (bx, by)) in enumerate(reports):
        max_dist = manhattan(sx, sy, bx, by)
        y_dist = abs(sy - TARGET)
        remaining_dist = max_dist - y_dist
        for i in range(sx - remaining_dist, sx + remaining_dist + 1):
            if (i, TARGET) not in beacons and (i, TARGET) not in sensors:
                impossible.add((i, TARGET))

    return len(impossible)

def main():
    with open("input/15.data") as f:
        reports = [line.strip() for line in f.readlines()]
        print(solve(reports))

if __name__ == "__main__":
    main()
