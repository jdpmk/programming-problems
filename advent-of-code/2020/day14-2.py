"""
--- Part Two ---
For some reason, the sea port's computer system still can't communicate with your ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
    If the bitmask bit is X, the corresponding memory address bit is floating.
    A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this means the floating bits will take on all possible values, potentially causing many memory addresses to be written all at once!

    For example, consider the following program:

        mask = 000000000000000000000000000000X1001X
        mem[42] = 100
        mask = 00000000000000000000000000000000X0XX
        mem[26] = 1
        When this program goes to write to memory address 42, it first applies the bitmask:

            address: 000000000000000000000000000000101010  (decimal 42)
            mask:    000000000000000000000000000000X1001X
            result:  000000000000000000000000000000X1101X
            After applying the mask, four bits are overwritten, three of which are different, and two of which are floating. Floating bits take on every possible combination of values; with two floating bits, four actual memory addresses are written:

                000000000000000000000000000000011010  (decimal 26)
                000000000000000000000000000000011011  (decimal 27)
                000000000000000000000000000000111010  (decimal 58)
                000000000000000000000000000000111011  (decimal 59)
                Next, the program is about to write to memory address 26 with a different bitmask:

                    address: 000000000000000000000000000000011010  (decimal 26)
                    mask:    00000000000000000000000000000000X0XX
                    result:  00000000000000000000000000000001X0XX
                    This results in an address with three floating bits, causing writes to eight memory addresses:

                        000000000000000000000000000000010000  (decimal 16)
                        000000000000000000000000000000010001  (decimal 17)
                        000000000000000000000000000000010010  (decimal 18)
                        000000000000000000000000000000010011  (decimal 19)
                        000000000000000000000000000000011000  (decimal 24)
                        000000000000000000000000000000011001  (decimal 25)
                        000000000000000000000000000000011010  (decimal 26)
                        000000000000000000000000000000011011  (decimal 27)
                        The entire 36-bit address space still begins initialized to the value 0 at every address, and you still need the sum of all values left in memory at the end of the program. In this example, the sum is 208.

                        Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum of all values left in memory after it completes?
"""

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
