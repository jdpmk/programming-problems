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
