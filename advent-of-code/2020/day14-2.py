BITS = 36

mem = {}

def pad_bin(num):
    bin_component = bin(num)[2:]
    leading = "0" * (BITS - len(bin_component))
    return leading + bin_component

def generate(s, i, val):
    while i >= 0 and s[i] != "X":
        i -= 1
    if i >= 0:
        generate(s[:i] + "0" + s[i + 1:], i - 1, val)
        generate(s[:i] + "1" + s[i + 1:], i - 1, val)
    else:
        mem[int(s, 2)] = int(val)

def process(mask, idx, val):
    idx = list(pad_bin(int(idx)))
    for i in reversed(range(BITS)):
        if mask[i] == "0":
            continue
        idx[i] = mask[i]

    generate("".join(idx), BITS - 1, val)

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
