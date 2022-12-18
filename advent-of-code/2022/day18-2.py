import math
import sys

sys.setrecursionlimit(10000)

AIR = 0
LAVA = 1

def solve(cubes):
    min_x, max_x = math.inf, -math.inf
    min_y, max_y = math.inf, -math.inf
    min_z, max_z = math.inf, -math.inf

    droplet = {}
    visited = set()
    lava = set()

    for x, y, z in cubes:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        min_z = min(min_z, z)
        max_z = max(max_z, z)
        lava.add((x, y, z))

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                droplet[(x, y, z)] = AIR

    num_sides_exposed = {}
    for x, y, z in cubes:
        droplet[(x, y, z)] = LAVA
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

            if (x_, y_, z_) in lava:
                sides_exposed -= 1

        num_sides_exposed[(x, y, z)] = sides_exposed

    def mark_cube(x, y, z, droplet, visited, mark):
        if not (min_x <= x <= max_x) or \
           not (min_y <= y <= max_y) or \
           not (min_z <= z <= max_z) or \
           (x, y, z) in visited or      \
           droplet[(x, y, z)] != mark:
               return

        visited.add((x, y, z))

        for dx, dy, dz in [(-1, 0, 0), \
                           (1, 0, 0),  \
                           (0, -1, 0), \
                           (0, 1, 0),  \
                           (0, 0, -1), \
                           (0, 0, 1)]:
            x_ = x + dx
            y_ = y + dy
            z_ = z + dz
            mark_cube(x_, y_, z_, droplet, visited, mark)

    def count_internal_surface_area(x, y, z, droplet, visited):
        if not (min_x <= x <= max_x) or \
           not (min_y <= y <= max_y) or \
           not (min_z <= z <= max_z) or \
           (x, y, z) in visited:
               return 0

        visited.add((x, y, z))

        internal_faces = 0

        for dx, dy, dz in [(-1, 0, 0), \
                           (1, 0, 0),  \
                           (0, -1, 0), \
                           (0, 1, 0),  \
                           (0, 0, -1), \
                           (0, 0, 1)]:
            x_ = x + dx
            y_ = y + dy
            z_ = z + dz

            if min_x <= x_ <= max_x and \
               min_y <= y_ <= max_y and \
               min_z <= z_ <= max_z and \
               droplet[(x_, y_, z_)] == LAVA:
                internal_faces += 1
            else:
                internal_faces += count_internal_surface_area(x_, y_, z_, droplet, visited)

        return internal_faces

    # try using the (min_x, min_y, min_z) as the initial position to mark
    # air cubes surrounding the droplet
    if droplet[(min_x, min_y, min_z)] != LAVA:
        mark_cube(min_x, min_y, min_z, droplet, visited, AIR)
    else:
        return None

    # air cubes around the droplet are marked visited. every air cube that is
    # not visited yet must be internal within the droplet
    internal_faces = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if (x, y, z) not in visited and droplet[(x, y, z)] == AIR:
                    internal_faces += \
                        count_internal_surface_area(x, y, z, droplet, visited)

    total_faces = sum(num_sides_exposed.values())
    return total_faces - internal_faces

def main():
    with open("input/18.data") as f:
        cubes = [tuple(map(int, line.strip().split(","))) for line in f.readlines()]
        print(solve(cubes))

if __name__ == "__main__":
    main()
