base16 = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

def product(xs):
    prod = 1
    for x in xs:
        prod *= x
    return prod

op = {
    0: sum,
    1: product,
    2: min,
    3: max,
    5: lambda l: 1 if l[0] > l[1] else 0,
    6: lambda l: 1 if l[0] < l[1] else 0,
    7: lambda l: 1 if l[0] == l[1] else 0
}

def bin_int(bin_str):
    total = 0
    for c in bin_str:
        total = total * 2 + int(c)
    return total

def parse(packet):
    if len(packet) < 11:
        return len(packet), None

    parent_version = bin_int(packet[0:3])
    parent_id = bin_int(packet[3:6])

    if parent_id == 4:
        literal = ""
        num_groups_read = 0
        i = 6

        while True:
            literal += packet[i + 1:i + 5]
            num_groups_read += 1
            i += 5
            if packet[i - 5] == '0':
                break

        return i, bin_int(literal)
    else:
        i = 6
        if packet[i] == '0':
            bits_remaining = bin_int(packet[7:22])
            subpacket_values = []
            i = 22

            while bits_remaining:
                idx_diff, subpacket_value = parse(packet[i:])
                i += idx_diff
                bits_remaining -= idx_diff

                if subpacket_value is not None:
                    subpacket_values.append(subpacket_value)
        else:
            num_subpackets = bin_int(packet[7:18])
            subpacket_values = []
            i = 18

            for _ in range(num_subpackets):
                idx_diff, subpacket_value = parse(packet[i:])
                i += idx_diff

                if subpacket_value is not None:
                    subpacket_values.append(subpacket_value)

        return i, op[parent_id](subpacket_values)

def solve(packet):
    packet = "".join([base16[c] for c in packet])
    _, value = parse(packet)

    return value

def main():
    with open("input/16.data") as f:
        packet = f.readline().strip()
        print(solve(packet))

if __name__ == "__main__":
    main()
