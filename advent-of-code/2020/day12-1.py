DIR = ["E", "S", "W", "N"]

def solve(data):
    dx, dy = 0, 0
    d_ptr = 0
    for line in data:
        d, v = line[:1], int(line[1:])
        if d in "LR":
            while v > 0:
                d_ptr = (d_ptr + (1 if d == "R" else -1)) % len(DIR)
                v -= 90
        if d == "F":
            d = DIR[d_ptr]
        if d in "NS":
            dy += v * (1 if d == "N" else -1)
        if d in "EW":
            dx += v * (1 if d == "E" else -1)
    return abs(dx) + abs(dy)

def main():
    with open("input/12.txt") as f:
        data = []
        for line in f:
            data.append(line.strip())
        print(solve(data))

if __name__ == "__main__":
    main()
