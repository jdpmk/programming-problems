SUBJECT_NUMBER = 7
MOD_FACTOR = 20201227

def determine_loop_size(subject_number, mod_factor, target):
    value = 1
    loop_size = 0
    while value != target:
        value = (value * subject_number) % mod_factor
        loop_size += 1
    return loop_size

def transform(mod_factor, public_key, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * public_key) % mod_factor
    return value

def solve(keys):
    loop_sizes = [determine_loop_size(SUBJECT_NUMBER, MOD_FACTOR, key) for key in keys]
    return transform(MOD_FACTOR, keys[0], loop_sizes[1])

def main():
    with open("input/25.txt") as f:
        data = []
        for line in f:
            data.append(int(line.strip()))
        print(solve(data))

if __name__ == "__main__":
    main()
