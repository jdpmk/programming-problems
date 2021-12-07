import math

def solve(xs):
    cheapest = math.inf

    for mid in range(min(xs), max(xs) + 1):
        cost = 0

        for x in xs:
            diff = abs(x - mid)
            cost += diff * (diff + 1) // 2

        cheapest = min(cheapest, cost)

    return cheapest

def main():
    with open("input/7.data") as f:
        xs = list(map(int, f.readline().strip().split(",")))
        print(solve(xs))

if __name__ == "__main__":
    main()
