import re

REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def check_valid(fields):
    for k, v in fields.items():
        if k == "byr":
            if not re.search("^(19[2-9][0-9]|200[0-2])$", v):
                return False
        if k == "iyr":
            if not re.search("^(201[0-9]|2020)$", v):
                return False
        if k == "eyr":
            if not re.search("^(202[0-9]|2030)$", v):
                return False
        if k == "hgt":
            if not re.search("(^(1([5-8][0-9]|9[0-3]))cm$)|(^((([5-6][0-9])|(7[0-6]))in$))", v):
                return False
        if k == "hcl":
            if not re.search("#[a-f0-9]{6}", v):
                return False
        if k == "ecl":
            if v not in "amb blu brn gry grn hzl oth".split():
                return False
        if k == "pid":
            if not re.search("^([0-9]{9})$", v):
                return False

    return True


def solve(data):
    valid = 0
    fields = {}
    for line in data:
        if not line:
            if False not in [requirement in fields.keys() for requirement in REQUIRED_FIELDS]:
                if check_valid(fields):
                    valid += 1
            fields.clear()
            continue
        for field in line.split():
            key, value = field.split(":")
            fields[key] = value
    if False not in [requirement in fields.keys() for requirement in REQUIRED_FIELDS]:
        if check_valid(fields):
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
