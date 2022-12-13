import functools

WRONG = 1
RIGHT = -1
CONT  = 0

def ordered(a, b):
    if type(a) == type(b) == int:
        if a < b: return RIGHT
        elif a == b: return CONT
        else: return WRONG

    if type(a) == type(b) == list:
        if not a and b: return RIGHT
        if not b and a: return WRONG
        if not a and not b: return CONT

        first = ordered(a[0], b[0])
        if first == WRONG: return WRONG
        if first == RIGHT: return RIGHT

        return ordered(a[1:], b[1:])

    if type(a) == int: a = [a]
    if type(b) == int: b = [b]
    return ordered(a, b)

def solve(packets):
    packets.append([[2]])
    packets.append([[6]])

    sorted_packets = sorted(packets, key=functools.cmp_to_key(ordered))
    p, q = -1, -1

    for i, packet in enumerate(sorted_packets):
        if packet == [[2]]:
            p = i + 1
        elif packet == [[6]]:
            q = i + 1

    return p * q

def main():
    with open("input/13.data") as f:
        contents = "\n".join(filter(None, (line.strip() for line in f.readlines())))
        packets = [eval(packet) for packet in contents.split("\n")]
        print(solve(packets))

if __name__ == "__main__":
    main()
