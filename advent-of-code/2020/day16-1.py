def solve(data):
    rules, my, other = data
    my = [int(num) for num in my[1].split(",")]
    other = [[int(num) for num in ticket.split(",")] for ticket in other[1:-1]]

    valid_ranges = []
    for rule in rules:
        ranges = rule.split(": ")[1]
        for rng in ranges.split(" or "):
            lb, ub = rng.split("-")
            valid_ranges.append(range(int(lb), int(ub) + 1))
    
    invalid_nums = []
    for num in my:
        if True not in [num in rng for rng in valid_ranges]:
            invalid_nums.append(num)

    for ticket in other:
        for num in ticket:
            if True not in [num in rng for rng in valid_ranges]:
                invalid_nums.append(num)
    
    return sum(invalid_nums)

def main():
    with open("input/16.txt") as f:
        data = ""
        for line in f:
            data += line
        components = [component.split("\n") for component in data.split("\n\n")]
        print(solve(components))

if __name__ == "__main__":
    main()
