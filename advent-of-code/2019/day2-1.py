with open("input/2.data") as f:
    program = list(map(int, f.read().strip().split(",")))

    n = len(program)
    pc = 0

    program[1] = 12
    program[2] = 2

    while pc < n:
        opcode = program[pc]

        if opcode == 1:
            x = program[pc + 1]
            y = program[pc + 2]
            dst = program[pc + 3]
            program[dst] = program[x] + program[y]
            pc += 4
        elif opcode == 2:
            x = program[pc + 1]
            y = program[pc + 2]
            dst = program[pc + 3]
            program[dst] = program[x] * program[y]
            pc += 4
        elif opcode == 99:
            break
        else:
            assert False, opcode

    print(program[0])
