class Cell:
    def __init__(self, value, marked=False):
        self.value = value
        self.marked = marked

    def __str__(self):
        return f"[ {self.value} | {self.marked} ]"

    def __repr__(self):
        return self.__str__()

def mark_and_check(boards, x, winners):
    round_winners = []

    for i, board in enumerate(boards):
        if i in winners:
            continue

        for j in range(len(board)):
            for k in range(len(board[j])):
                if board[j][k].value == x:
                    board[j][k].marked = True

        for j in range(len(board)):
            if all([board[j][k].marked for k in range(len(board[j]))]):
                round_winners.append(i)

        for k in range(len(board[0])):
            if all([board[j][k].marked for j in range(len(board))]):
                round_winners.append(i)

    return round_winners

def score(boards, i):
    return sum([boards[i][j][k].value for j in range(len(boards[i])) for k in range(len(boards[i][j])) if not boards[i][j][k].marked])

def solve(boards, xs):
    winners = set()
    scores = []

    for i, x in enumerate(xs):
        round_winners = mark_and_check(boards, x, winners)
        for winner in round_winners:
            winners.add(winner)
            scores.append(x * score(boards, winner))

    return scores[-1]

def main():
    with open("input/4.data") as f:
        xs = list(map(int, f.readline().strip().split(",")))
        f.readline()

        boards = []
        board = []

        for line in f.readlines():
            line = line.strip()

            if not line:
                boards.append(board)
                board = []
            else:
                board.append(list(map(Cell, map(int, line.split()))))

        boards.append(board)

        print(solve(boards, xs))

if __name__ == "__main__":
    main()
