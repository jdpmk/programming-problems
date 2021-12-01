def solve(measurements):
    ct = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            ct += 1

    return ct

def main():
    with open("input/1.data") as f:
        measurements = list(map(lambda line: int(line.strip()), f.readlines()))
        print(solve(measurements))

if __name__ == "__main__":
    main()
