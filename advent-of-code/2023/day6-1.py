def solve(ts, ds):
    n = len(ts)
    assert n == len(ds)

    prod = 1
    for i in range(n):
        ways = 0
        for j in range(1, ts[i]):
            if j * (ts[i] - j) > ds[i]:
                ways += 1
        prod *= ways

    return prod

def main():
    with open("input/6.data") as f:
        ts = list(map(int, f.readline().split(":")[1].strip().split()))
        ds = list(map(int, f.readline().split(":")[1].strip().split()))
        print(solve(ts, ds))

if __name__ == "__main__":
    main()
