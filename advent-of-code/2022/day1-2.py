import heapq

def solve(items):
    curr_sum = 0
    top3 = []

    for item in items:
        if item:
            curr_sum += int(item)
        else:
            heapq.heappush(top3, curr_sum)
            if len(top3) > 3:
                heapq.heappop(top3)
            curr_sum = 0

    heapq.heappush(top3, curr_sum)
    if len(top3) > 3:
        heapq.heappop(top3)

    return sum(top3)

def main():
    with open("input/1.data") as f:
        data = [line.strip() for line in f.readlines()]
        print(solve(data))

if __name__ == "__main__":
    main()
