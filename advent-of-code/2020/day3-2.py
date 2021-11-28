"""
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

    What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

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
