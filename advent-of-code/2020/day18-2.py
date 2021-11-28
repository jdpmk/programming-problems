"""
--- Part Two ---
You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

    1 + 2 * 3 + 4 * 5 + 6
      3   * 3 + 4 * 5 + 6
        3   *   7   * 5 + 6
          3   *   7   *  11
               21       *  11
                        231
                        Here are the other examples from above:

                            1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
                            2 * 3 + (4 * 5) becomes 46.
                            5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
                            5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
                            ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
                            What do you get if you add up the results of evaluating the homework problems using these new rules?
"""

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
