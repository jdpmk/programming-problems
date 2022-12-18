def solve(cubes):
    cube_set = set()
    for cube in cubes:
        cube_set.add(cube)

    num_sides_exposed = {}

    for x, y, z in cubes:
        sides_exposed = 6
        for dx, dy, dz in [(-1, 0, 0), \
                           (1, 0, 0),  \
                           (0, -1, 0), \
                           (0, 1, 0),  \
                           (0, 0, -1), \
                           (0, 0, 1)]:
            x_ = x + dx
            y_ = y + dy
            z_ = z + dz

            if (x_, y_, z_) in cube_set:
                sides_exposed -= 1

        num_sides_exposed[(x, y, z)] = sides_exposed

    return sum(num_sides_exposed.values())

def main():
    with open("input/18.data") as f:
        cubes = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
        print(solve(cubes))

if __name__ == "__main__":
    main()
