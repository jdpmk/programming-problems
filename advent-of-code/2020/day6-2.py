def solve(data):
    total = 0
    unique = set()
    for group in data:
        responses = [set(person) for person in group.split("\n") if person]
        total += len(set.intersection(*responses))
    return total

def main():
    with open("input/6.txt") as f:
        data = ""
        for line in f:
            data += line
        print(solve(data.split("\n\n")))

if __name__ == "__main__":
    main()
