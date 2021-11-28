"""
--- Part Two ---
The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

    byr valid:   2002
    byr invalid: 2003

    hgt valid:   60in
    hgt valid:   190cm
    hgt invalid: 190in
    hgt invalid: 190

    hcl valid:   #123abc
    hcl invalid: #123abz
    hcl invalid: 123abc

    ecl valid:   brn
    ecl invalid: wat

    pid valid:   000000001
    pid invalid: 0123456789
    Here are some invalid passports:

    eyr:1972 cid:100
    hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

    iyr:2019
    hcl:#602927 eyr:1967 hgt:170cm
    ecl:grn pid:012533040 byr:1946

    hcl:dab227 iyr:2012
    ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

    hgt:59cm ecl:zzz
    eyr:2038 hcl:74454a iyr:2023
    pid:3556412378 byr:2007
    Here are some valid passports:

    pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
    hcl:#623a2f

    eyr:2029 ecl:blu cid:129 byr:1989
    iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

    hcl:#888785
    hgt:164cm byr:2001 iyr:2015 cid:88
    pid:545766238 ecl:hzl
    eyr:2022

    iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
    Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
"""

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
