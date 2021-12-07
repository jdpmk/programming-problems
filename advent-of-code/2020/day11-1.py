def within_bounds(i, j, M, N):
    return not(i < 0 or i > M - 1 or j < 0 or j > N - 1)

def solve(data):
    M, N = len(data), len(data[0])
    result = [[data[i][j] for j in range(N)] for i in range(M)]
    DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    change = True
    while change:
        change = False
        for i in range(M):
            for j in range(N):
                num_occupied = 0
                for direction in DIRS:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    if within_bounds(new_i, new_j, M, N):
                        if data[new_i][new_j] == '#':
                            num_occupied += 1
                if data[i][j] == 'L' and num_occupied == 0:
                    change = True
                    result[i][j] = '#'
                if data[i][j] == '#' and num_occupied >= 4:
                    change = True
                    result[i][j] = 'L'
        data = [[result[i][j] for j in range(N)] for i in range(M)]

    occupied_steady_state = 0
    for i in range(M):
        for j in range(N):
            if result[i][j] == '#':
                occupied_steady_state += 1
    return occupied_steady_state

def main():
    with open("input/11.txt") as f:
        data = []
        for line in f:
            data.append(line.strip())
        print(solve(data))

if __name__ == "__main__":
    main()
