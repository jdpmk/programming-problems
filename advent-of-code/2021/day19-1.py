import collections
import math

rs = [
    lambda v: [v[0], v[1], v[2]],
    lambda v: [v[0], -v[2], v[1]],
    lambda v: [v[0], -v[1], -v[2]],
    lambda v: [v[0], v[2], -v[1]],
    lambda v: [-v[0], -v[1], v[2]],
    lambda v: [-v[0], -v[2], -v[1]],
    lambda v: [-v[0], v[1], -v[2]],
    lambda v: [-v[0], v[2], v[1]],
    lambda v: [-v[2], v[0], -v[1]],
    lambda v: [v[1], v[0], -v[2]],
    lambda v: [v[2], v[0], v[1]],
    lambda v: [-v[1], v[0], v[2]],
    lambda v: [v[2], -v[0], -v[1]],
    lambda v: [v[1], -v[0], v[2]],
    lambda v: [-v[2], -v[0], v[1]],
    lambda v: [-v[1], -v[0], -v[2]],
    lambda v: [-v[1], -v[2], v[0]],
    lambda v: [v[2], -v[1], v[0]],
    lambda v: [v[1], v[2], v[0]],
    lambda v: [-v[2], v[1], v[0]],
    lambda v: [v[2], v[1], -v[0]],
    lambda v: [-v[1], v[2], -v[0]],
    lambda v: [-v[2], -v[1], -v[0]],
    lambda v: [v[1], -v[2], -v[0]]
]

translate = lambda v, w: [v[i] + w[i] for i in range(len(v))]

def solve(scanners):
    source = scanners[0]
    found = set()
    matched_scanners = set()
    source_matched = [True] * len(source)
    d = 0

    for v in source:
        found.add(tuple(v))

    tss = []
    for scanner in scanners:
        ts = []
        for f, rfn in enumerate(rs):
            ts.append(list(map(lambda v: rfn(v), scanner)))
        tss.append(ts)

    while True:
        if len(matched_scanners) == len(scanners):
            break

        if d in matched_scanners:
            d = 1 if d + 1 == len(scanners) else d + 1
            continue

        b = scanners[d]
        matched = False
        for i, u in enumerate(source):
            for f, rfn in enumerate(rs):
                tb = tss[d][f]
                for j, v in enumerate(tb):
                    diff = [u[0] - v[0], u[1] - v[1], u[2] - v[2]]
                    for r in range(len(tb)):
                        tb[r] = [tb[r][0] + diff[0], tb[r][1] + diff[1], tb[r][2] + diff[2]]

                    ct = 0
                    for jj, vv in enumerate(tb):
                        if tuple(vv) in found:
                            ct += 1

                    if ct >= 12:
                        matched = True
                        matched_scanners.add(d)

                        for jj, vv in enumerate(tb):
                            if tuple(vv) not in found:
                                found.add(tuple(vv))
                                source.append(vv)

                    if matched:
                        break
                if matched:
                    break
            if matched:
                break

        d = 1 if d + 1 == len(scanners) else d + 1

    return len(source)

def main():
    with open("input/19.data") as f:
        contents = "".join(f.readlines())
        scanners = [list(map(lambda b: list(map(int, b.split(","))), s.split("\n")[1:])) for s in contents.split("\n\n")]
        print(solve(scanners))

if __name__ == "__main__":
    main()
