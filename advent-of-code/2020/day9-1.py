def find_sums(data, l, r):
    sums = []
    for i in range(l, r):
        for j in range(l, r):
            if i != j:
                sums.append(data[i] + data[j])
    return sums

def solve(data):
    l, r = 0, 25
    while r < len(data):
        if data[r] not in find_sums(data, l, r):
            return data[r]
        l += 1
        r += 1
    return -1

def main():
    with open("input/9.txt") as f:
        data = []
        for line in f:
            data.append(int(line.strip()))
        print(solve(data))

if __name__ == "__main__":
    main()
