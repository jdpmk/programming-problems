def solve(cups):
    N = len(cups)
    cmin, cmax = min(cups), max(cups)
    i = 0
    used = list()
    for _ in range(100):
        curr = cups[i]
        nextc = cups[(i + 4) % N]
        a, b, c = (i + 1) % N, (i + 2) % N, (i + 3) % N
        picked = [a, b, c]
        [used.append(cups[x]) for x in picked]
        for cup in used:
            cups.remove(cup)
        dest = curr - 1
        while dest >= cmin and dest in used:
            dest -= 1
        if dest < cmin:
            dest = cmax
            while dest in used:
                dest -= 1
        dest_idx = cups.index(dest)
        insert_at = (dest_idx + 1) % N
        for cup in used:
            cups.insert(insert_at, cup)
            insert_at = (insert_at + 1) % N
        picked.clear()
        used.clear()
        i = cups.index(nextc)

    i = 0
    while cups[i] != 1:
        i += 1
    i += 1
    out = ""
    while cups[i] != 1:
        out += str(cups[i])
        i = (i + 1) % N
    return out

def main():
    with open("input/23.txt") as f:
        print(solve([int(e) for e in f.readlines()[0].strip()]))

if __name__ == "__main__":
    main()
