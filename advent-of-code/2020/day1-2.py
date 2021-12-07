def solve(data, target):
    seen = set()
    for num in data:
        seen.add(num)

    for i in range(len(data)):
        for j in range(len(data)):
            complement = target - data[i] - data[j]
            if complement in seen:
                return data[i] * data[j] * complement

    return -1

def main():
    data = []
    with open("input/1.txt") as f:
        for line in f:
            data.append(int(line))
    
    target = 2020
    print(solve(data, target))

if __name__ == "__main__":
    main()
