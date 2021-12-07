def solve(data, target):
    seen = set()
    for num in data:
        complement = target - num
        if complement in seen:
            return complement * num
        seen.add(num)
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
