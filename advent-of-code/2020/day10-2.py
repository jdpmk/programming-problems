"""
--- Part Two ---
To completely determine whether you have enough adapters, you'll need to figure out how many different ways they can be arranged. Every arrangement needs to connect the charging outlet to your device. The previous rules about when adapters can successfully connect still apply.

The first example above (the one that starts with 16, 10, 15) supports the following arrangements:

    (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
    (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
    (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
    (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
    (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
    (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
    (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
    (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
    (The charging outlet and your device's built-in adapter are shown in parentheses.) Given the adapters from the first example, the total number of arrangements that connect the charging outlet to your device is 8.

            The second example above (the one that starts with 28, 33, 18) has many arrangements. Here are a few:

                (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
                32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)

                (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
                32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)

                (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
                32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)

                (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
                32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)

                (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
                32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)

                (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
                46, 48, 49, (52)

                (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
                46, 49, (52)

                (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
                47, 48, 49, (52)

                (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
                47, 49, (52)

                (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
                48, 49, (52)
                In total, this set of adapters can connect the charging outlet to your device in 19208 distinct arrangements.

                You glance back down at your bag and try to remember why you brought so many adapters; there must be more than a trillion valid ways to arrange them! Surely, there must be an efficient way to count the arrangements.

                What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
"""

import numpy as np

def solve(data):
    data = data + [0, max(data) + 3]
    data.sort()
    idx = 0
    m = {}
    adj = np.zeros((len(data), len(data)))
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                if data[i] - data[j] in range(1, 4):
                    if data[j] not in m:
                        m[data[j]] = idx
                        idx += 1
                    if data[i] not in m:
                        m[data[i]] = idx
                        idx += 1
                    adj[m[data[j]]][m[data[i]]] = 1
    
    ans = 0
    original = np.array(adj)
    for i in range(len(data)):
        adj = adj @ original
        ans += adj[m[min(data)]][m[max(data)]]
    return int(ans)

def main():
    with open("input/10.txt") as f:
        data = []
        for line in f:
            data.append(int(line.strip()))
        print(solve(data))

if __name__ == "__main__":
    main()
