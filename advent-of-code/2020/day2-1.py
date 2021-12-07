def solve(data):
    num_valid = 0
    for line in data:
        policy, password = line.split(": ")
        bounds, target = policy.split()
        lb, ub = [int(b) for b in bounds.split("-")]

        count = 0
        for c in password:
            if c == target:
                count += 1
        if lb <= count <= ub:
            num_valid += 1

    return num_valid

def main():
    data = []
    with open("input/2.txt") as f:
        for line in f:
            data.append(line)

    print(solve(data))

if __name__ == "__main__":
    main()
