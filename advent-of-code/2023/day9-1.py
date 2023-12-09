def next_of(seq):
    last_of = [seq[-1]]
    while True:
        next_seq = []
        all_zeros = True
        i = 0
        while i < len(seq) - 1:
            v = seq[i + 1] - seq[i]
            if v: all_zeros = False
            next_seq.append(v)
            i += 1
        last_of.append(next_seq[-1])
        if all_zeros:
            break
        seq = next_seq

    i = len(last_of) - 2
    while i >= 0:
        last_of[i] = last_of[i] + last_of[i + 1]
        i -= 1

    return last_of[0]

def solve(seqs):
    total = 0
    for seq in seqs:
        total += next_of(seq)
    return total

def main():
    with open("input/9.data") as f:
        seqs = [list(map(int, s.strip().split())) for s in f.readlines()]
        print(solve(seqs))

if __name__ == "__main__":
    main()
