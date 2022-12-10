import collections

def solve(insts):
    x = 1
    c = 1
    q = collections.deque()
    for inst in insts:
        if inst == "noop":
            c += 1
            continue
        _, V = inst.split()
        q.append((c + 2, int(V)))
        c += 2

    crt = [["." for _ in range(40)] for _ in range(6)]
    c = 1
    while q:
        if q[0][0] == c:
            _, V = q.popleft()
            x += V
        crty = (c - 1) // 40
        crtx = (c - 1) % 40
        if crtx in [x - 1, x, x + 1]:
            crt[crty][crtx] = "#"
        c += 1

    return "\n".join("".join(row) for row in crt)

def main():
    with open("input/10.data") as f:
        instructions = [line.strip() for line in f.readlines()]
        print(solve(instructions))

if __name__ == "__main__":
    main()
