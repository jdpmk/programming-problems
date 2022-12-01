def solve(items):
    return max(sum(int(item) for item in elf.split("\n")) for elf in items.split("\n\n"))

def main():
    with open("input/1.data") as f:
        data = "\n".join(line.strip() for line in f.readlines())
        print(solve(data))

if __name__ == "__main__":
    main()
