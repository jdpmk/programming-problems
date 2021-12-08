def solve(entries):
    ct = 0

    for entry in entries:
        _, rhs = entry.split(" | ")
        rhs = rhs.split()
        ct += len(list(filter(lambda e: e in [2, 3, 4, 7], map(len, rhs))))

    return ct

def main():
    with open("input/8.data") as f:
        entries = [line.strip() for line in f.readlines()]
        print(solve(entries))

if __name__ == "__main__":
    main()
