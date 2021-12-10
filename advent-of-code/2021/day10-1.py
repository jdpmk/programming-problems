import collections

table = {
    None: 0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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
                return c
            if s.pop() != complement[c]:
                return c
        else:
            s.append(c)

    return None

def solve(chunks):
    return sum([table[first_invalid_char(chunk)] for chunk in chunks])

def main():
    with open("input/10.data") as f:
        chunks = [line.strip() for line in f.readlines()]
        print(solve(chunks))

if __name__ == "__main__":
    main()
