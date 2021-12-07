def solve(data):
    total = 0
    unique = set()
    for group in data:
        for person in group.split("\n"):
            [unique.add(question) for question in set(person)]
        total += len(unique)
        unique.clear()
    return total

def main():
    with open("input/6.txt") as f:
        data = ""
        for line in f:
            data += line
        print(solve(data.split("\n\n")))

if __name__ == "__main__":
    main()
