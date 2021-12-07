def solve(data):
    num_valid = 0
    for line in data:
        policy, password = line.split(": ")
        bounds, c = policy.split()
        lb, ub = [int(b) for b in bounds.split("-")]

        only_one = (password[lb - 1] == c) ^ (password[ub - 1] == c)
        if only_one:
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
