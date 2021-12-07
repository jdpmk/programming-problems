def r(data, acc, curr, seen, goal, used):
    if curr in seen:
        return None
    if curr == goal:
        return acc

    seen.add(curr)
    instruction, value = data[curr].split()
    value = int(value)

    if instruction == "acc":
        return r(data, acc + value, curr + 1, seen, goal, used)
    if instruction == "jmp":
        return r(data, acc, curr + value, seen, goal, used) or (r(data, acc, curr + 1, seen, goal, True) if not used else None)
    if instruction == "nop":
        return r(data, acc, curr + 1, seen, goal, used) or (r(data, acc, curr + value, seen, goal, True) if not used else None)

def solve(data):
    return r(data, 0, 0, set(), len(data), False)

def main():
    with open("input/8.txt") as f:
        data = []
        for line in f:
            data.append(line)
        print(solve(data))

if __name__ == "__main__":
    main()
