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
