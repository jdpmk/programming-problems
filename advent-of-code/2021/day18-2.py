import re

pair_finder = re.compile(".*\[[0-9]+,[0-9]+\]")

def explode(expr):
    o = 0
    s4 = None
    for i, c in enumerate(expr):
        if c == '[':
            o += 1
            if o == 4:
                s4 = i
        elif c == ']':
            o -= 1
            if o < 4:
                s4 = None

        if s4 is not None:
            match = pair_finder.match(expr[s4 + 1:i + 1])
            if not match:
                continue

            s, e = match.span()
            s += s4 + 1
            e += s4 + 1

            ss = expr[s:e].rindex("[") + s4 + 1
            ci = expr[ss:e].index(",") + s4 + 1 + ss - s

            l = int(expr[ss + 1:ci])
            r = int(expr[ci + 1:e - 1])

            lis = -1
            for lie in range(ss, -1, -1):
                if expr[lie].isdigit():
                    lis = lie
                    while lis >= 0 and expr[lis].isdigit():
                        lis -= 1
                    break

            if lie == 0:
                expr_lhs = expr[:ss] + "0"
            else:
                expr_lhs = expr[:lis + 1] + str(int(expr[lis + 1:lie + 1]) + l) + expr[lie + 1:ss] + "0"

            rie = -1
            for ris in range(e - 1, len(expr)):
                if expr[ris].isdigit():
                    rie = ris
                    while rie < len(expr) and expr[rie].isdigit():
                        rie += 1
                    break

            if ris == len(expr) - 1:
                expr_rhs = expr[e:]
            else:
                expr_rhs = expr[e:ris] + str(int(expr[ris:rie]) + r) + expr[rie:]

            expr = expr_lhs + expr_rhs
            return expr

    return expr

def split(expr):
    for i in range(len(expr)):
        j = i
        while expr[j].isdigit():
            j += 1

        if j < i + 2:
            continue

        x = int(expr[i:j])
        expr = expr[:i] + f"[{x // 2},{(x + 1) // 2}]" + expr[j:]
        return expr

    return expr

def simplify(expr):
    while True:
        exploded = explode(expr)
        if exploded != expr:
            expr = exploded
            continue

        splitted = split(exploded)
        if splitted != expr:
            expr = splitted
            continue

        return expr

def magnitude(expr):
    if isinstance(expr, int):
        return expr
    return 3 * magnitude(expr[0]) + 2 * magnitude(expr[1])

def solve(nums):
    max_magnitude = 0

    for i, a in enumerate(nums):
        for j, b in enumerate(nums):
            if i != j:
                max_magnitude = max(max_magnitude, magnitude(eval(simplify("[" + a + "," + b + "]"))))

    return max_magnitude

def main():
    with open("input/18.data") as f:
        nums = [line.strip() for line in f.readlines()]
        print(solve(nums))

if __name__ == "__main__":
    main()
