INF = float('inf')

def solve(time, shuttles):
    pairs = []
    for i in range(len(shuttles)):
        if shuttles[i] == 'x':
            continue
        pairs.append((int(shuttles[i]), i))

    idx = 1
    step = pairs[0][0]
    t = step
    while idx < len(pairs):
        if (t + pairs[idx][1]) % pairs[idx][0] == 0:
            step *= pairs[idx][0]
            idx += 1
            if idx == len(pairs):
                return t
        t += step

    return t

def main():
    with open("input/13.txt") as f:
        contents = [element.strip() for element in f.readlines()]
        time = int(contents[0])
        shuttles = contents[1]
        print(solve(time, shuttles.split(",")))

if __name__ == "__main__":
    main()
