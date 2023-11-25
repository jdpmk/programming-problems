with open("input/1.data") as f:
    masses = [int(line.strip()) for line in f.readlines()]
    print(sum(map(lambda x: x // 3 - 2, masses)))
