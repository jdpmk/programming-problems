def solve(data):
    distribution = {}
    prev = 0
    data.sort()
    for i in range(len(data)):
        curr = data[i]
        distribution[curr - prev] = distribution.get(curr - prev, 0) + 1
        prev = curr
    mine = max(data) + 3
    distribution[mine - prev] = distribution.get(mine - prev, 0) + 1
    return distribution[1] * distribution[3]

def main():
    with open("input/10.txt") as f:
        data = []
        for line in f:
            data.append(int(line.strip()))
        print(solve(data))

if __name__ == "__main__":
    main()
