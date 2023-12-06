def solve(t, d):
    ways = 0
    for j in range(1, t):
        if j * (t - j) > d:
            ways += 1
    return ways

def main():
    with open("input/6.data") as f:
        ts = int("".join(c for c in f.readline().split(":")[1] if c.isdigit()))
        ds = int("".join(c for c in f.readline().split(":")[1] if c.isdigit()))
        print(solve(ts, ds))

if __name__ == "__main__":
    main()
