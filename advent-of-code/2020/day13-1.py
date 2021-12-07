import math

INF = float('inf')

def solve(time, shuttles):
    next_times = [INF] * len(shuttles)
    min_times = INF
    for i in range(len(shuttles)):
        shuttle = shuttles[i]
        if shuttle == "x":
            continue
        shuttle = int(shuttle)
        next_times[i] = math.ceil(time / shuttle)
        if next_times[i] < min_times:
            min_times = next_times[i]
            min_idx = i

    return int(shuttles[min_idx]) * (int(shuttles[min_idx]) * next_times[min_idx] - time)

def main():
    with open("input/13.txt") as f:
        contents = [element.strip() for element in f.readlines()]
        time = int(contents[0])
        shuttles = contents[1]
        print(solve(time, shuttles.split(",")))

if __name__ == "__main__":
    main()
