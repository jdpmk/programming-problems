import collections
import operator

OPS = {
    "+": operator.add,
    "*": operator.mul
}

def index_of(s, c):
    for i in range(len(s)):
        if s[i] == c:
            return i
    return -1

def evaluate(exp):
    while index_of(exp, "(") != -1:
        i = index_of(exp, "(")
        if i != -1:
            s = collections.deque([i])
            while s:
                j = i + 1
                while j < len(exp) and exp[j] != ")":
                    if exp[j] == "(":
                        s.append(j)
                    j += 1
                start = s.pop()
                exp = exp[:start] + [evaluate(exp[start + 1: j])] + exp[j + 1:]
    for op, fn in OPS.items():
        while index_of(exp, op) != -1:
           k = index_of(exp, op)
           exp = exp[:k - 1] + [fn(exp[k - 1], exp[k + 1])] + exp[k + 2:]
    return exp[0]

def solve(expressions):
    exps = [[int(x) if x in "1234567890" else x for x in [e for e in exp if e != " "]] for exp in expressions]
    return sum([evaluate(exp) for exp in exps])

def main():
    with open("input/18.txt") as f:
        data = []
        for line in f:
            data.append(line.strip())
        print(solve(data))

if __name__ == "__main__":
    main()
