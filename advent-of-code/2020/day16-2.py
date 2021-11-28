"""
--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use the remaining valid tickets to determine which field is which.

Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if seat is the third field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

    class: 0-1 or 4-19
    row: 0-5 or 8-19
    seat: 0-13 or 16-19

    your ticket:
        11,12,13

        nearby tickets:
            3,9,18
            15,1,5
            5,14,9
            Based on the nearby tickets in the above example, the first position must be row, the second position must be class, and the third position must be seat; you can conclude that in your ticket, class is 12, row is 11, and seat is 13.

            Once you work out which field is which, look for the six fields on your ticket that start with the word departure. What do you get if you multiply those six values together?
"""

def solve(data):
    rules, my, other = data
    my = [int(num) for num in my[1].split(",")]
    other = [[int(num) for num in ticket.split(",")] for ticket in other[1:-1]]

    all_ranges = []
    desired_ranges = {}
    for rule in rules:
        label, ranges = rule.split(": ")
        this_label_ranges = []
        for rng in ranges.split(" or "):
            lb, ub = rng.split("-")
            this_label_ranges.append(range(int(lb), int(ub) + 1))
        desired_ranges[label] = this_label_ranges
        all_ranges += desired_ranges[label]

    invalid_nums = set()
    for num in my:
        if True not in [num in rng for rng in all_ranges]:
            invalid_nums.add(num)
    for ticket in other:
        for num in ticket:
            if True not in [num in rng for rng in all_ranges]:
                invalid_nums.add(num)

    other = [ticket for ticket in other if not any(num in invalid_nums for num in ticket)]
    all_tickets = [my] + other

    transpose = []
    for i in range(len(all_tickets[1])):
        col = []
        for j in range(len(all_tickets)):
            col.append(all_tickets[j][i])
        transpose.append(col)

    possibilities = {}
    for label, ranges in desired_ranges.items():
        for i in range(len(transpose)):
            col = transpose[i]
            match = True
            for num in col:
                valid = False
                for rng in ranges:
                    valid = valid or num in rng
                match = match and valid
            if match:
                possibilities[label] = possibilities.get(label, []) + [i]

    used = set()
    possibilities = {k: v for k, v in sorted(possibilities.items(), key=lambda x: len(x[1]))}
    actual = {}
    departure_cols = []
    for label, options in possibilities.items():
        for option in options:
            if option not in used:
                if "departure" in label:
                    departure_cols.append((label, option))
                actual[label] = option
                used.add(option)

    product = 1
    for col in departure_cols:
        product *= my[col[1]]

    return product

def main():
    with open("input/16.txt") as f:
        data = ""
        for line in f:
            data += line
        components = [component.split("\n") for component in data.split("\n\n")]
        print(solve(components))

if __name__ == "__main__":
    main()
