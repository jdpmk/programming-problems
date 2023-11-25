import sys

with open("input/2.data") as f:
    original = list(map(int, f.read().strip().split(",")))

    n = len(original)

    for noun in range(100):
        for verb in range(100):
            program = list(original)

            pc = 0
            program[1] = noun
            program[2] = verb

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

            if program[0] == 19690720:
                print("{}{}".format(noun, verb))
                sys.exit()
