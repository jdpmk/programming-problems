def solve(lines):
    digit = lambda c: "0" <= c <= "9"
    words = ["one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine"]

    def tokenize(s):
        n = len(s)
        nums = []

        for i, c in enumerate(s):
            if digit(c):
                nums.append((i, int(c)))

        for i, word in enumerate(words):
            m = len(word)
            j = 0

            while j < n:
                if j + m - 1 < n and s[j:j + m] == word:
                    nums.append((j, i + 1))
                    j += m
                else:
                    j += 1

        nums.sort()
        return [value for (_, value) in nums]

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
