def solve(template, rules):
    rules = {k: v for k, v in rules}

    pairs = {}
    freq = {}

    for i in range(1, len(template)):
        pattern = template[i - 1: i + 1]
        pairs[pattern] = pairs.get(pattern, 0) + 1
    for c in template:
        freq[c] = freq.get(c, 0) + 1

    num_iterations = 40
    for _ in range(num_iterations):
        for (a, b), ct in pairs.copy().items():                         # ex. NN occurs x times
            if a + b in rules:                                          # make sure there's a rule for NN
                to_insert = rules[a + b]                                # determine what to insert: NN -> C
                pairs[a + b] -= ct                                      # remove x occurrences of NN
                pairs[a + to_insert] = pairs.get(a + to_insert, 0) + ct # add x occurrences of NC
                pairs[to_insert + b] = pairs.get(to_insert + b, 0) + ct # add x occurrences of CN
                freq[to_insert] = freq.get(to_insert, 0) + ct           # add x occurrences of inserted character

    return max(freq.values()) - min(freq.values())

def main():
    with open("input/14.data") as f:
        template = f.readline().strip()
        f.readline()
        rules = [line.strip().split(" -> ") for line in f.readlines()]

        print(solve(template, rules))

if __name__ == "__main__":
    main()
