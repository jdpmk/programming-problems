def intify(l):
    n = len(l)
    x = 0

    for i, e in enumerate(l):
        x += e * 2 ** (n - i - 1)

    return x

def solve(xs):
    n = len(xs)
    m = len(xs[0])

    gamma = []
    epsilon = []

    for i in range(m):
        num_ones = 0
        for j in range(n):
            if xs[j][i] == '1':
                num_ones += 1

        gamma.append(0 + (num_ones > n / 2))
        epsilon.append(1 - (num_ones > n / 2))

    return intify(gamma) * intify(epsilon)
            
def main():
    with open("input/3.data") as f:
        xs = list(map(lambda line: line.strip(), f.readlines()))
        print(solve(xs))

if __name__ == "__main__":
    main()
