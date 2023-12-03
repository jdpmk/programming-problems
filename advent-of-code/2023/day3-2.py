def seek(g, v, i, j, m, n):
    while j >= 0 and g[i][j].isdigit() and not v[i][j]:
        v[i][j] = True
        j -= 1
    j += 1

    total = 0
    while j < n and g[i][j].isdigit():
        v[i][j] = True
        total = 10 * total + int(g[i][j])
        j += 1

    return total

def gear(c):
    return c == '*'

def solve(g):
    m, n = len(g), len(g[0])
    v = [[False for _ in range(n)] for _ in range(m)]

    nums = {}
    for i in range(m):
        for j in range(n):
            if gear(g[i][j]):
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if not di and not dj: continue
                        i_ = i + di
                        j_ = j + dj
                        if not v[i_][j_] and g[i_][j_].isdigit():
                            num = seek(g, v, i_, j_, m, n)
                            nums[(i, j)] = nums.get((i, j), []) + [num]

    ratio = 0
    for _, nums in nums.items():
        if len(nums) == 2:
            ratio += nums[0] * nums[1]

    return ratio

def main():
    with open("input/3.data") as f:
        schematic = [line.strip() for line in f.readlines()]
        print(solve(schematic))

if __name__ == "__main__":
    main()
