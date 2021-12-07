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
