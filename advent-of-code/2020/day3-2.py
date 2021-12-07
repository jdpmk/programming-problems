def solve(data):
    M, N = len(data), len(data[0])

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    results = []
    for dx, dy in slopes:
        num_trees = 0
        i, j = 0, 0
        while i < M:
            if data[i][j % N] == '#':
                num_trees += 1
            i += dy
            j += dx
        results.append(num_trees)

    product = 1
    for num in results:
        product *= num
    
    return product

def main():
    data = []
    with open("input/3.txt") as f:
        for line in f:
            data.append(list(line.strip()))
    
    print(solve(data))

if __name__ == "__main__":
    main()
