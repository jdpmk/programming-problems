def solve(cards):
    total = 0

    for card in cards:
        elfs, mine = card.split(" | ")
        elfs = set(map(int, elfs.split()))
        mine = map(int, mine.split())

        value = None
        for num in mine:
            if num in elfs:
                value = 1 if value is None else value << 1

        total += value or 0

    return total

def main():
    with open("input/4.data") as f:
        cards = [line.strip().split(": ")[1] for line in f.readlines()]
        print(solve(cards))

if __name__ == "__main__":
    main()
