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
            return m

        def get_from_map(m, x):
            for d, s, n in m:
                if s <= x <= s + n:
                    return d + x - s
            return x

        m1 = read_next_map()
        m2 = read_next_map()
        m3 = read_next_map()
        m4 = read_next_map()
        m5 = read_next_map()
        m6 = read_next_map()
        m7 = read_next_map()

        min_location = math.inf
        for seed in seeds:
            x = get_from_map(m1, seed)
            x = get_from_map(m2, x)
            x = get_from_map(m3, x)
            x = get_from_map(m4, x)
            x = get_from_map(m5, x)
            x = get_from_map(m6, x)
            x = get_from_map(m7, x)
            min_location = min(min_location, x)

        print(min_location)

if __name__ == "__main__":
    main()
