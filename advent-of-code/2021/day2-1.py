def solve(instructions):
    x = 0
    y = 0

    for direction, magnitude in instructions:
        magnitude = int(magnitude)
        if direction == "forward":
            x += magnitude
        if direction == "down":
            y += magnitude
        if direction == "up":
            y -= magnitude

    return x * y

def main():
    with open("input/2.data") as f:
        instructions = list(map(lambda line: line.strip().split(), f.readlines()))
        print(solve(instructions))

if __name__ == "__main__":
    main()
