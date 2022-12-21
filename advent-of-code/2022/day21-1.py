def get_op(task):
    if "+" in task: return "+"
    if "-" in task: return "-"
    if "*" in task: return "*"
    if "/" in task: return "/"

def get_fun(op):
    if op == "+": return lambda a, b: a + b
    if op == "-": return lambda a, b: a - b
    if op == "*": return lambda a, b: a * b
    if op == "/": return lambda a, b: a // b

def solve(monkeys):
    g = {}
    for monkey, task in monkeys:
        try:
            g[monkey] = int(task)
        except:
            op = get_op(task)
            g[monkey] = (get_fun(op), *task.split(" {} ".format(op)))

    def helper(g, u):
        if type(g[u]) == int:
            return g[u]

        op, l, r = g[u]
        return op(helper(g, l), helper(g, r))

    return helper(g, 'root')

def main():
    with open("input/21.data") as f:
        monkeys = [line.strip().split(": ") for line in f.readlines()]
        print(solve(monkeys))

if __name__ == "__main__":
    main()
