import collections

table = {
    None: 0,
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

complement = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

def is_close(c):
    return c in [')', ']', '}', '>']

def first_invalid_char(chunk):
    s = collections.deque()
    for c in chunk:
        if is_close(c):
            if not s:
                return c, s
            if s.pop() != complement[c]:
                return c, s
        else:
            s.append(c)

    return None, s

def solve(chunks):
    all_points = []
    for chunk in chunks:
        c, s = first_invalid_char(chunk)
        if not c:
            complete = []
            while s:
                complete.append(complement[s.pop()])

            points = 0
            for c in complete:
                points = points * 5 + table[c]
            all_points.append(points)

    return sorted(all_points)[len(all_points) // 2]

def main():
    with open("input/10.data") as f:
        chunks = [line.strip() for line in f.readlines()]
        print(solve(chunks))

if __name__ == "__main__":
    main()
