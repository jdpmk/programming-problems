def solve(template, rules):
    rules = {k: v for k, v in rules}

    num_iterations = 10
    for _ in range(num_iterations):
        i = 1
        while i < len(template):
            if template[i - 1: i + 1] in rules:
                template = template[:i] + rules[template[i - 1: i + 1]] + template[i:]
                i += 1
            i += 1

    freq = {}
    for c in template:
        freq[c] = freq.get(c, 0) + 1

    return max(freq.values()) - min(freq.values())

def main():
    with open("input/14.data") as f:
        template = f.readline().strip()
        f.readline()
        rules = [line.strip().split(" -> ") for line in f.readlines()]

        print(solve(template, rules))

if __name__ == "__main__":
    main()
