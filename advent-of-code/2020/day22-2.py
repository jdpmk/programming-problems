import collections

def play(p1, p2, g=1, r=1):
    seen = set()
    p1 = collections.deque(p1)
    p2 = collections.deque(p2)

    while p1 and p2:
        if (tuple(p1), tuple(p2)) in seen:
            return "p1", p1
        seen.add((tuple(p1), tuple(p2)))
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 <= len(p1) and c2 <= len(p2):
            winner, _ = play(list(p1)[:c1], list(p2)[:c2], g=g+1)
            if winner == "p1":
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        r += 1

    return ("p1", p1) if p1 and not p2 else ("p2", p2)

def solve(data):
    p1, p2 = data
    p1 = [int(card) for card in p1[1:] if card]
    p2 = [int(card) for card in p2[1:] if card]
    _, win= play(p1, p2)

    score = 0
    idx = 1
    while win:
        score += win.pop() * idx
        idx += 1

    return score

def main():
    with open("input/22.sample") as f:
        data = ""
        for line in f:
            data += line
        print(solve([player.split("\n") for player in data.split("\n\n")]))

if __name__ == "__main__":
    main()
