def intify(l):
    n = len(l)
    x = 0

    for i, e in enumerate(l):
        x += e * 2 ** (n - i - 1)

    return x

def oxy_rec(xs, i):
    n = len(xs)

    if n == 1:
        return list(map(int, xs[0]))

    num_ones = 0
    for j in range(n):
        if xs[j][i] == '1':
            num_ones += 1

    if num_ones >= n / 2:
        return oxy_rec(list(filter(lambda x: x[i] == '1', xs)), i + 1)
    else:
        return oxy_rec(list(filter(lambda x: x[i] == '0', xs)), i + 1)

def co2_rec(xs, i):
    n = len(xs)

    if n == 1:
        return list(map(int, xs[0]))

    num_ones = 0
    for j in range(n):
        if xs[j][i] == '1':
            num_ones += 1

    if num_ones < n / 2:
        return co2_rec(list(filter(lambda x: x[i] == '1', xs)), i + 1)
    else:
        return co2_rec(list(filter(lambda x: x[i] == '0', xs)), i + 1)    

def solve(xs):
    return intify(oxy_rec(xs, 0)) * intify(co2_rec(xs, 0))

def main():
    with open("input/3.data") as f:
        xs = list(map(lambda line: line.strip(), f.readlines()))
        print(solve(xs))

if __name__ == "__main__":
    main()
