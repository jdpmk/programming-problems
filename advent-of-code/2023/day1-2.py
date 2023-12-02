def solve(lines):
    words = ["one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine"]

    def tokenize(s):
        n = len(s)
        nums = []

        for i, c in enumerate(s):
            if c.isdigit():
                nums.append(int(c))
            else:
                for j, word in enumerate(words):
                    if s[i:i + len(word)] == word:
                        nums.append(j + 1)

        return nums

    total = 0
    for line in lines:
        nums = tokenize(line)
        total += nums[0] * 10 + nums[-1]

    return total

def main():
    with open("input/1.data") as f:
        lines = [line.strip() for line in f.readlines()]
        print(solve(lines))

if __name__ == "__main__":
    main()
