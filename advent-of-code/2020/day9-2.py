"""
--- Part Two ---
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576
    In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

    To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

    What is the encryption weakness in your XMAS-encrypted list of numbers?
"""

def solve(data):
    target = 530627549
    l, r = 0, 1
    sum_so_far = data[0] + data[1]
    while r < len(data) - 1:
        if sum_so_far < target:
            r += 1
            sum_so_far += data[r]
        elif sum_so_far > target:
            l += 1
            sum_so_far -= data[l - 1]
        else:
            rng = data[l:r + 1]
            return min(rng) + max(rng)
    return -1

def main():
    with open("input/9.txt") as f:
        data = []
        for line in f:
            data.append(int(line.strip()))
        print(solve(data))

if __name__ == "__main__":
    main()
