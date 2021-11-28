"""
--- Part Two ---
Impressed, the Elves issue you a challenge: determine the 30000000th number spoken. For example, given the same starting numbers as above:

    Given 0,3,6, the 30000000th number spoken is 175594.
    Given 1,3,2, the 30000000th number spoken is 2578.
    Given 2,1,3, the 30000000th number spoken is 3544142.
    Given 1,2,3, the 30000000th number spoken is 261214.
    Given 2,3,1, the 30000000th number spoken is 6895259.
    Given 3,2,1, the 30000000th number spoken is 18.
    Given 3,1,2, the 30000000th number spoken is 362.
    Given your starting numbers, what will be the 30000000th number spoken?
"""

turns = {}

def seen_once(num):
    return num in turns and not turns[num][1]

def seen_twice(num):
    return num in turns and turns[num][1] is not None

def update(num, turn):
    if num not in turns:
        turns[num] = (turn, None)
        return
    if not turns[num][1]:
        turns[num] = (turns[num][0], turn)
    else:
        turns[num] = (turns[num][1], turn)

def solve(nums):
    N = len(nums)
    last = nums[0]
    for i in range(N):
        turns[nums[i]] = (i + 1, None)
        last = nums[i]

    for j in range(i + 1, 30000000):
        if seen_once(last):
            spoken = 0
        if seen_twice(last):
            spoken = turns[last][1] - turns[last][0]
        update(spoken, j + 1)
        last = spoken
    
    return last

def main():
    with open("input/15.txt") as f:
        line = f.readline()
        print(solve([int(num) for num in line.strip().split(",")]))

if __name__ == "__main__":
    main()
