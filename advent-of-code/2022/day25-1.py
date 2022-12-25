import math
import collections

digit = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2
}

def convert_dec_to_snafu(x):
    as_snafu = []

    while x:
        m = x % 5
        x = x // 5 + (m > 2)
        if m == 0: 
            as_snafu.append("0")
        if m == 1: 
            as_snafu.append("1")
        if m == 2: 
            as_snafu.append("2")
        if m == 3: 
            as_snafu.append("=")
        if m == 4: 
            as_snafu.append("-")

    return reversed(as_snafu)

def solve(nums):
    total = 0

    for num in nums:
        for i, d in enumerate(num):
            total += 5 ** (len(num) - i - 1) * digit[d]

    return "".join(convert_dec_to_snafu(total))

def main():
    with open("input/25.data") as f:
        nums = [line.strip() for line in f.readlines()]
        print(solve(nums))

if __name__ == "__main__":
    main()
