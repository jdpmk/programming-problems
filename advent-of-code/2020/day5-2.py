"""
--- Part Two ---
Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""

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
