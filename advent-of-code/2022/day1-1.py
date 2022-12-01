def solve(items):
    max_sum = 0
    curr_sum = 0

    for item in items:
        if item:
            curr_sum += int(item)
        else:
            max_sum = max(max_sum, curr_sum)
            curr_sum = 0

    max_sum = max(max_sum, curr_sum)

    return max_sum

def main():
    with open("input/1.data") as f:
        data = [line.strip() for line in f.readlines()]
        print(solve(data))

if __name__ == "__main__":
    main()
