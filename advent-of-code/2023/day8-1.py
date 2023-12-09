def solve(pattern, nodes):
    m = len(pattern)

    gl, gr = {}, {}
    for n, l, r in nodes:
        gl[n] = l
        gr[n] = r

    steps = 0
    i = 0
    n = "AAA"

    while True:
        if n == "ZZZ":
            return steps
        n = (gl if pattern[i] == "L" else gr)[n]
        i = (i + 1) % m
        steps += 1

    assert False

def parse_node(s):
    n, lr = s.split(" = ")
    l, r = lr.split(", ")
    return n, l[1:], r[:-1]

def main():
    with open("input/8.data") as f:
        lines = [line.strip() for line in f.readlines()]
        pattern = lines[0]
        nodes = [parse_node(line) for line in lines[2:]]
        print(solve(pattern, nodes))

if __name__ == "__main__":
    main()
