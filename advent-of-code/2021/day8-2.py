def solve(entries):
    total = 0

    displays = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9
    }

    for entry in entries:
        segment = {}
        lhs, rhs = entry.split(" | ")

        lhs = lhs.split()
        rhs = rhs.split()

        freq = {}
        for pattern in lhs:
            for c in pattern:
                freq[c] = freq.get(c, 0) + 1

        # segment corresponding to a appears in 7 but not in 1
        for pattern1 in lhs:
            if len(pattern1) != 2: continue
            for pattern2 in lhs:
                if len(pattern2) != 3: continue
                for c in pattern2:
                    if c not in pattern1:
                        segment['a'] = c

        # segment corresponding to
        # - e occurs 4 times
        # - b occurs 6 times
        # - f occurs 9 times
        for k, v in freq.items():
            if v == 4:
                segment['e'] = k
            elif v == 6:
                segment['b'] = k
            elif v == 9:
                segment['f'] = k

        # segment corresponding to c is the last remaining in 7 (a, c, f)
        for pattern in lhs:
            if len(pattern) == 3 and segment['a'] in pattern and segment['f'] in pattern:
                for c in pattern:
                    if c not in [segment['a'], segment['f']]:
                        segment['c'] = c
                        break

        # segment corresponding to d is the last remaining in 4 (b, c, d, f)
        for pattern in lhs:
            if len(pattern) == 4:
                for c in pattern:
                    if c not in segment.values():
                        segment['d'] = c
                        break

        # last segment corresponds to g
        for c in "abcdefg":
            if c not in segment.values():
                segment['g'] = c
                break

        segment_rev = {v: k for k, v in segment.items()}

        entry_total = 0
        for pattern in rhs:
            s = "".join(sorted([segment_rev[c] for c in pattern]))
            entry_total = 10 * entry_total + displays[s]

        total += entry_total

    return total

def main():
    with open("input/8.data") as f:
        entries = [line.strip() for line in f.readlines()]
        print(solve(entries))

if __name__ == "__main__":
    main()
