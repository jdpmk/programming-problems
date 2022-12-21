LEFT = False
RIGHT = True

NO_HUMN = False
HAS_HUMN = True

def get_op_id(task):
    if "+" in task: return "+"
    if "-" in task: return "-"
    if "*" in task: return "*"
    if "/" in task: return "/"

def get_fun(op_id):
    if op_id == "+": return lambda a, b: a + b
    if op_id == "-": return lambda a, b: a - b
    if op_id == "*": return lambda a, b: a * b
    if op_id == "/": return lambda a, b: a // b

def solve(monkeys):
    g = {}
    for monkey, task in monkeys:
        try:
            g[monkey] = int(task)
        except:
            op_id = get_op_id(task)
            g[monkey] = ((op_id, get_fun(op_id)), *task.split(" {} ".format(op_id)))

    def find(g, u, q, sides):
        if u == q:
            return True

        if type(g[u]) == int:
            return False

        _, l, r = g[u]

        found = find(g, l, q, sides)
        if found:
            sides.append(LEFT)
            return found

        found = find(g, r, q, sides)
        if found:
            sides.append(RIGHT)
            return found

    def compute(g, u, side):
        if type(g[u]) == int:
            return g[u]

        (_, op), l, r = g[u]

        if u == "root":
            return compute(g, l, side) if side == LEFT else compute(g, r, side)
        return op(compute(g, l, side), compute(g, r, side))

    def backsolve(g, u, sides, humn, target):
        if humn == NO_HUMN:
            if type(g[u]) == int:
                return g[u]

            (_, op), l, r = g[u]
            return op(backsolve(g, l, sides, humn, target),
                      backsolve(g, r, sides, humn, target))

        else:
            # if we're at "humn" we can update our required
            # value and stop
            if u == "humn":
                g[u] = target
                return

            (op_id, _), l, r = g[u]

            # at each step, one side contains the "humn" node
            # and the other side has a value which can be
            # directly computed
            humn_side = sides[0]
            other_side = not humn_side
            other_u = l if other_side == LEFT else r
            humn_u = l if humn_side == LEFT else r

            next_sides = sides[1:]

            # compute the proper modification to the target value
            # ex. current target = 2022 * (...)
            #     where 2022 is the value of the "other" branch
            #     and (...) represents the evaluation of the branch
            #     where the "humn" node exists. therefore, we know
            #     that (...) must evaluate to the value of
            #     target / 2022.
            # these rules are a bit more complicated for subtraction
            # and division since the operations are not commutative
            def get_new_target(op_id, t, o, h):
                if op_id == "+":
                    return t - o
                if op_id == "-":
                    if h == LEFT:
                        return t + o
                    else:
                        return o - t
                if op_id == "*":
                    return t // o
                if op_id == "/":
                    if h == LEFT:
                        return t * o
                    else:
                        return o // t

            # backsolve the other value and calculate the target
            other_value = backsolve(g, other_u, next_sides, NO_HUMN, target)
            assert other_value is not None
            new_target = get_new_target(op_id, target, other_value, humn_side)

            # the operation at "root" is equality, so don't use the target until
            # the first "actual" node
            if u == "root":
                return backsolve(g, humn_u, next_sides, HAS_HUMN, target)

            return backsolve(g, humn_u, next_sides, HAS_HUMN, new_target)

    # find the steps to get to "humn" from "root"
    sides = []
    found = find(g, "root", "humn", sides)
    assert found
    sides.reverse()

    # compute the value needed to match at the root
    # on the side of the tree which "humn" is NOT on
    target = compute(g, "root", not sides[0])

    # compute the required value for "humn". this
    # modifies the value stored at g["humn"]
    backsolve(g, "root", sides, HAS_HUMN, target)

    return g["humn"]

def main():
    with open("input/21.data") as f:
        monkeys = [line.strip().split(": ") for line in f.readlines()]
        print(solve(monkeys))

if __name__ == "__main__":
    main()
