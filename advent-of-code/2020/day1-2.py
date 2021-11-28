"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

def solve(data, target):
    seen = set()
    for num in data:
        seen.add(num)

    for i in range(len(data)):
        for j in range(len(data)):
            complement = target - data[i] - data[j]
            if complement in seen:
                return data[i] * data[j] * complement

    return -1

def main():
    data = []
    with open("input/1.txt") as f:
        for line in f:
            data.append(int(line))
    
    target = 2020
    print(solve(data, target))

if __name__ == "__main__":
    main()
