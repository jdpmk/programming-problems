REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def solve(data):
    valid = 0
    fields = {}
    for line in data:
        if not line:
            if False not in [requirement in fields.keys() for requirement in REQUIRED_FIELDS]:
                valid += 1
            fields.clear()
            continue
        for field in line.split():
            key, value = field.split(":")
            fields[key] = value
    if False not in [requirement in fields.keys() for requirement in REQUIRED_FIELDS]:
        valid += 1
    return valid

def main():
    with open("input/4.txt") as f:
        data = []
        for line in f:
            data.append(line.strip())
        print(solve(data))

if __name__ == "__main__":
    main()
