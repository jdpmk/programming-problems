def solve(measurements):
    sliding_sum = lambda measurements, i: sum(measurements[i:i + 3])
    sliding_sums = [sliding_sum(measurements, i) for i in range(len(measurements) - 2)]

    ct = 0
    for i in range(1, len(sliding_sums)):
        if sliding_sums[i] > sliding_sums[i - 1]:
            ct += 1

    return ct

def main():
    with open("input/1.data") as f:
        measurements = list(map(lambda line: int(line.strip()), f.readlines()))
        print(solve(measurements))

if __name__ == "__main__":
    main()
