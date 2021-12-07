INF = float('inf')

def bsp(s, lo, hi, l, r):
    for c in s:
        if lo < hi:
            mid = (lo + hi) // 2
            if c == l:
                hi = mid
            else:
                lo = mid

    return lo

def solve(data):
    max_seat_id = -INF
    seats = []

    for boarding_pass in data:
        row = bsp(boarding_pass[:7], 0, 128, "F", "B")
        col = bsp(boarding_pass[7:], 0, 8, "L", "R")
        this_seat_id = row * 8 + col
        seats.append(this_seat_id)
        max_seat_id = max(max_seat_id, this_seat_id)
    
    seats.sort()
    for i in range(len(seats) - 1):
        if seats[i] + 2 == seats[i + 1]:
            return seats[i] + 1

    return -1

def main():
    with open("input/5.txt") as f:
        data = []
        for line in f:
            data.append(line)
        print(solve(data))

if __name__ == "__main__":
    main()
