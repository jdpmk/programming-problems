class Cell:
    def __init__(self, value, marked=False):
        self.value = value
        self.marked = marked

    def __str__(self):
        return f"[ {self.value} | {self.marked} ]"

    def __repr__(self):
        return self.__str__()

def mark(boards, x):
    for i, board in enumerate(boards):
        for j in range(len(board)):
            for k in range(len(board[j])):
                if board[j][k].value == x:
                    board[j][k].marked = True

def find_winner(boards):
    for i, board in enumerate(boards):
        for j in range(len(board)):
            if all([board[j][k].marked for k in range(len(board[j]))]):
                return i

        for k in range(len(board[0])):
            if all([board[j][k].marked for j in range(len(board))]):
                return i

    return None

def score(boards, i):
    return sum([boards[i][j][k].value for j in range(len(boards[i])) for k in range(len(boards[i][j])) if not boards[i][j][k].marked])

def solve(boards, xs):
    for x in xs:
        mark(boards, x)
        winner = find_winner(boards)
        if winner is not None:
            return x * score(boards, winner)

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
