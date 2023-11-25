def calculate(fuel):
    total = 0
    while True:
        fuel = fuel // 3 - 2
        if fuel <= 0:
            break
        total += fuel
    return total

with open("input/1.data") as f:
    masses = [int(line.strip()) for line in f.readlines()]
    print(sum(map(calculate, masses)))
