def solve(lines):
    digit = lambda c: "0" <= c <= "9"

    total = 0

    for line in lines:
        for c in line:
            if digit(c):
                total += 10 * int(c)
                break
        for c in reversed(line):
            if digit(c):
                total += int(c)
                break

    return total

def main():
    with open("input/1.data") as f:
        lines = [line.strip() for line in f.readlines()]
        print(solve(lines))

if __name__ == "__main__":
    main()
