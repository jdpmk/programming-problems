def solve(cards):
    total = 0

    ct = {i: 1 for i in range(len(cards))}

    for i, card in enumerate(cards):
        elfs, mine = card.split(" | ")
        elfs = set(map(int, elfs.split()))
        mine = map(int, mine.split())

        value = 0
        for num in mine:
            if num in elfs:
                value += 1

        for j in range(value):
            ct[i + 1 + j] += ct[i]

    return sum(ct.values())

def main():
    with open("input/4.data") as f:
        cards = [line.strip().split(": ")[1] for line in f.readlines()]
        print(solve(cards))

if __name__ == "__main__":
    main()
