def solve(data):
    M, N = len(data), len(data[0])
    i, j = 0, 0
    
    num_trees = 0
    while i < M:
        if data[i][j % N] == '#':
            num_trees += 1
        i += 1
        j += 3

    return num_trees

def main():
    data = []
    with open("input/3.txt") as f:
        for line in f:
            data.append(list(line.strip()))
    
    print(solve(data))

if __name__ == "__main__":
    main()
