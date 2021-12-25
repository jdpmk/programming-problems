import copy

def advance(region):
    advanced = False
    cp = copy.deepcopy(region)
    m, n = len(cp), len(cp[0])

    for i in range(m):
        for j in range(n):
            if region[i][j] == '>' and region[i][(j + 1) % n] == '.':
                advanced = True
                cp[i][(j + 1) % n] = '>'
                cp[i][j] = '.'

    region = cp
    cp = copy.deepcopy(region)

    for i in range(m):
        for j in range(n):
            if region[i][j] == 'v' and region[(i + 1) % m][j] == '.':
                advanced = True
                cp[(i + 1) % m][j] = 'v'
                cp[i][j] = '.'

    return cp, advanced

def solve(region):
    step = 0

    while True:
        region, advanced = advance(region)
        step += 1

        if not advanced:
            break

    return step

def main():
    with open("input/25.data") as f:
        region = [list(line.strip()) for line in f.readlines()]
        print(solve(region))

if __name__ == "__main__":
    main()
