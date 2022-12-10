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

    total = 0
    c = 1
    while q:
        if q[0][0] == c:
            _, V = q.popleft()
            x += V
        if c in [20, 60, 100, 140, 180, 220]:
            total += c * x
        c += 1

    return total

def main():
    with open("input/10.data") as f:
        instructions = [line.strip() for line in f.readlines()]
        print(solve(instructions))

if __name__ == "__main__":
    main()
