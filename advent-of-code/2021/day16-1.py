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

def bin_int(bin_str):
    total = 0
    for c in bin_str:
        total = total * 2 + int(c)
    return total

def parse(packet, versions):
    if len(packet) < 8:
        return len(packet)

    parent_version = bin_int(packet[0:3])
    parent_id = bin_int(packet[3:6])

    versions.append(parent_version)

    if parent_id == 4:
        num_groups_read = 0
        i = 6

        while True:
            num_groups_read += 1
            i += 5
            if packet[i - 5] == '0':
                break

        return i
    else:
        i = 6
        if packet[i] == '1':
            num_subpackets = bin_int(packet[7:18])
            i = 18
        else:
            num_subpackets = bin_int(packet[7:22])
            i = 22

        for _ in range(num_subpackets):
            i += parse(packet[i:], versions)

        return i

def solve(packet):
    packet = "".join([base16[c] for c in packet])
    versions = []
    parse(packet, versions)
    return sum(versions)

def main():
    with open("input/16.data") as f:
        packet = f.readline().strip()
        print(solve(packet))

if __name__ == "__main__":
    main()
