def too_far(hr, hc, tr, tc):
    return max(abs(hr - tr), abs(hc - tc)) >= 2

def solve(steps):
    lr, lc = 0, 0
    hr, hc = 0, 0
    tr, tc = 0, 0

    visited = set()
    visited.add((0, 0))

    for step in steps:
        direction, magnitude = step.split()
        magnitude = int(magnitude)

        for _ in range(magnitude):
            if direction == "U":
                lr, lc = hr, hc
                hr += 1
            elif direction == "D":
                lr, lc = hr, hc
                hr -= 1
            elif direction == "L":
                lr, lc = hr, hc
                hc -= 1
            else:
                lr, lc = hr, hc
                hc += 1

            if too_far(hr, hc, tr, tc):
                tr, tc = lr, lc
                visited.add((tr, tc))

    return len(visited)

def main():
    with open("input/9.data") as f:
        steps = [line.strip() for line in f.readlines()]
        print(solve(steps))

if __name__ == "__main__":
    main()
