def solve(lines):
    total = 0

    for line in lines:
        for c in line:
            if c.isdigit():
                total += 10 * int(c)
                break
        for c in reversed(line):
            if c.isdigit():
                total += int(c)
                break

    return total

def main():
    with open("input/1.data") as f:
        lines = [line.strip() for line in f.readlines()]
        print(solve(lines))

if __name__ == "__main__":
    main()
