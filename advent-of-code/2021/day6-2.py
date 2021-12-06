def solve(xs, days=256):
    freq = {}
    for x in xs:
        freq[x] = freq.get(x, 0) + 1

    for _ in range(days):
        new_freq = {}
        for k, v in freq.items():
            if k == 0:
                new_freq[8] = v
                new_freq[6] = new_freq.get(6, 0) + v
            else:
                new_freq[k - 1] = new_freq.get(k - 1, 0) + v
        freq = new_freq

    ct = 0
    for _, v in freq.items():
        ct += v

    return ct

def main():
    with open("input/6.data") as f:
        xs = list(map(int, f.readline().strip().split(",")))
        print(solve(xs))

if __name__ == "__main__":
    main()
