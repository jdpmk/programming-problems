def solve(instructions):
    x = 0
    y = 0
    aim = 0

    for direction, magnitude in instructions:
        magnitude = int(magnitude)
        if direction == "forward":
            x += magnitude
            y += aim * magnitude
        if direction == "down":
            aim += magnitude
        if direction == "up":
            aim -= magnitude

    return x * y

def main():
    with open("input/2.data") as f:
        instructions = list(map(lambda line: line.strip().split(), f.readlines()))
        print(solve(instructions))

if __name__ == "__main__":
    main()
