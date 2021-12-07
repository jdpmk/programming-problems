import collections

def solve(data):
    p1, p2 = data
    p1 = collections.deque([int(card) for card in p1[1:] if card])
    p2 = collections.deque([int(card) for card in p2[1:] if card])
    
    while p1 and p2:
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        elif c1 < c2:
            p2.append(c2)
            p2.append(c1)

    winning_score = 0
    idx = 1
    while p1:
        winning_score += p1.pop() * idx
        idx += 1
    while p2:
        winning_score += p2.pop() * idx
        idx += 1
    return winning_score

def main():
    with open("input/22.txt") as f:
        data = ""
        for line in f:
            data += line
        print(solve([player.split("\n") for player in data.split("\n\n")]))

if __name__ == "__main__":
    main()
