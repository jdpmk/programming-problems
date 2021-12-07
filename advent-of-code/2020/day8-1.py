def solve(data):
    seen = set()
    curr = 0
    acc = 0
    while curr not in seen:
        seen.add(curr)
        instruction, value = data[curr].split()
        value = int(value)
        if instruction == "acc":
            acc += value
        if instruction == "jmp":
            curr += value
        else:
            curr += 1

    return acc

def main():
    with open("input/8.txt") as f:
        data = []
        for line in f:
            data.append(line)
        print(solve(data))

if __name__ == "__main__":
    main()
