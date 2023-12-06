import math

def main():
    with open("input/5.data") as f:
        seeds = list(map(int, f.readline().strip().split(": ")[1].split()))
        f.readline()

        def read_next_map():
            m = []
            l = f.readline().strip()
            while True:
                l = f.readline().strip()
                if not l: break
                d, s, n = map(int, l.split())
                m.append((d, s, n))
            m.sort(key=lambda x: x[1])

            to_add = []
            acc = 0
            for _, s, n in m:
                len_to_add = s - acc
                if len_to_add:
                    to_add.append((acc, acc, len_to_add))
                acc = s + n
            to_add.append((acc, acc, 1000000000))

            m.extend(to_add)
            m.sort(key=lambda x: x[1])
            return m

        def get_ranges_from_map(m, b, k):
            ranges = []
            for d, s, n in m:
                l, h = s, s + n - 1
                ml, mh = b, b + k - 1
                if mh < l or h < ml:
                    continue
                l = max(l, ml)
                h = min(h, mh)
                ranges.append((d + l - s, h - l + 1))
            return ranges

        def get(m, ranges):
            ranges_ = []
            for b, k in ranges:
                ranges_.extend(get_ranges_from_map(m, b, k))
            return ranges_

        def apply(b, k):
            x = [(b, k)]
            x = get(m1, x)
            x = get(m2, x)
            x = get(m3, x)
            x = get(m4, x)
            x = get(m5, x)
            x = get(m6, x)
            x = get(m7, x)
            return x

        m1 = read_next_map()
        m2 = read_next_map()
        m3 = read_next_map()
        m4 = read_next_map()
        m5 = read_next_map()
        m6 = read_next_map()
        m7 = read_next_map()

        min_location = math.inf
        i = 0
        while i < len(seeds):
            b, k = seeds[i], seeds[i + 1]
            x = apply(b, k)
            min_location = min(min_location, min(map(lambda e: e[0], x)))
            i += 2

        print(min_location)

if __name__ == "__main__":
    main()
