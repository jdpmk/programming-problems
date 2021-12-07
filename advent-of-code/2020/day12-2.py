DIR = ["E", "S", "W", "N"]

def solve(data):
    sx, sy = 0, 0
    wx, wy = 10, 1
    x_ptr, y_ptr = 0, 3
    for line in data:
        d, v = line[:1], int(line[1:])
        if d in "LR":
            while v > 0:
                x_ptr = (x_ptr + (1 if d == "R" else -1)) % len(DIR)
                y_ptr = (y_ptr + (1 if d == "R" else -1)) % len(DIR)
                x_ptr, y_ptr = y_ptr, x_ptr
                wx, wy = wy, wx
                v -= 90
        if d == "F":
            while v:
                sx += wx * (1 if DIR[x_ptr] == "E" else -1)
                sy += wy * (1 if DIR[y_ptr] == "N" else -1)
                v -= 1
        if d in "NS":
            wy += v * (1 if d == DIR[y_ptr] else -1)
        if d in "EW":
            wx += v * (1 if d == DIR[x_ptr] else -1)
    return abs(sx) + abs(sy)

def main():
    with open("input/12.txt") as f:
        data = []
        for line in f:
            data.append(line.strip())
        print(solve(data))

if __name__ == "__main__":
    main()
