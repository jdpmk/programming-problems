BITS = 36

mem = {}

def pad_bin(num):
    bin_component = bin(num)[2:]
    leading = "0" * (BITS - len(bin_component))
    return leading + bin_component

def process(mask, idx, val):
    val = pad_bin(int(val))
    res = list(val)
    for i in reversed(range(BITS)):
        if mask[i] == "X":
            continue
        res[i] = mask[i]
    mem[idx] = int("".join(res), 2)

def solve(data):
    for line in data:
        if "mask" in line:
            m = line.split(" = ")[1]
        if "mem" in line:
            loc, val = line.split(" = ")
            idx = loc.split("[")[1][:-1]
            process(m, idx, val)

    return sum(mem.values())

def main():
    with open("input/14.txt") as f:
        data = []
        for line in f:
            data.append(line.strip())
        print(solve(data))

if __name__ == "__main__":
    main()
