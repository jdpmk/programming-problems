def solve(xs, days=80):
    for _ in range(days):
        new = []
        for i in range(len(xs)):
            xs[i] -= 1
            if xs[i] == -1:
                new.append(8)
                xs[i] = 6
        xs.extend(new)

    return len(xs)

def main():
    with open("input/6.data") as f:
        xs = list(map(int, f.readline().strip().split(",")))
        print(solve(xs))

if __name__ == "__main__":
    main()
