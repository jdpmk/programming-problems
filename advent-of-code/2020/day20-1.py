"""
--- Day 20: Jurassic Jigsaw ---
The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

    Tile 2311:
    ..##.#..#.
    ##..#.....
    #...##..#.
    ####.#...#
    ##.##.###.
    ##...#.###
    .#.#.#..##
    ..#....#..
    ###...#.#.
    ..###..###

    Tile 1951:
    #.##...##.
    #.####...#
    .....#..##
    #...######
    .##.#....#
    .###.#####
    ###.##.##.
    .###....#.
    ..#.#..#.#
    #...##.#..

    Tile 1171:
    ####...##.
    #..##.#..#
    ##.#..#.#.
    .###.####.
    ..###.####
    .##....##.
    .#...####.
    #.##.####.
    ####..#...
    .....##...

    Tile 1427:
    ###.##.#..
    .#..#.##..
    .#.##.#..#
    #.#.#.##.#
    ....#...##
    ...##..##.
    ...#.#####
    .#.####.#.
    ..#..###.#
    ..##.#..#.

    Tile 1489:
    ##.#.#....
    ..##...#..
    .##..##...
    ..#...#...
    #####...#.
    #..#.#.#.#
    ...#.#.#..
    ##.#...##.
    ..##.##.##
    ###.##.#..

    Tile 2473:
    #....####.
    #..#.##...
    #.##..#...
    ######.#.#
    .#...#.#.#
    .#########
    .###.#..#.
    ########.#
    ##...##.#.
    ..###.#.#.

    Tile 2971:
    ..#.#....#
    #...###...
    #.#.###...
    ##.##..#..
    .#####..##
    .#..####.#
    #..#.#..#.
    ..####.###
    ..#.#.###.
    ...#.#.#.#

    Tile 2729:
    ...#.#.#.#
    ####.#....
    ..#.#.....
    ....#..#.#
    .##..##.#.
    .#.####...
    ####.#.#..
    ##.####...
    ##..#.##..
    #.##...##.

    Tile 3079:
    #.#.#####.
    .#..######
    ..#.......
    ######....
    ####.#..#.
    .#...#.##.
    #.#####.##
    ..#.###...
    ..#.......
    ..#.###...
    By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

    #...##.#.. ..###..### #.#.#####.
    ..#.#..#.# ###...#.#. .#..######
    .###....#. ..#....#.. ..#.......
    ###.##.##. .#.#.#..## ######....
    .###.##### ##...#.### ####.#..#.
    .##.#....# ##.##.###. .#...#.##.
    #...###### ####.#...# #.#####.##
    .....#..## #...##..#. ..#.###...
    #.####...# ##..#..... ..#.......
    #.##...##. ..##.#..#. ..#.###...

    #.##...##. ..##.#..#. ..#.###...
    ##..#.##.. ..#..###.# ##.##....#
    ##.####... .#.####.#. ..#.###..#
    ####.#.#.. ...#.##### ###.#..###
    .#.####... ...##..##. .######.##
    .##..##.#. ....#...## #.#.#.#...
    ....#..#.# #.#.#.##.# #.###.###.
    ..#.#..... .#.##.#..# #.###.##..
    ####.#.... .#..#.##.. .######...
    ...#.#.#.# ###.##.#.. .##...####

    ...#.#.#.# ###.##.#.. .##...####
    ..#.#.###. ..##.##.## #..#.##..#
    ..####.### ##.#...##. .#.#..#.##
    #..#.#..#. ...#.#.#.. .####.###.
    .#..####.# #..#.#.#.# ####.###..
    .#####..## #####...#. .##....##.
    ##.##..#.. ..#...#... .####...#.
    #.#.###... .##..##... .####.##.#
    #...###... ..##...#.. ...#..####
    ..#.#....# ##.#.#.... ...##.....
    For reference, the IDs of the above tiles are:

    1951    2311    3079
    2729    1427    2473
    2971    1489    1171
    To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

    Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?
"""

from numpy import rot90 as R
from numpy import fliplr as H
from numpy import flipud as V
import numpy as np

OPS = {
    "I": [lambda x: x],
    "R": [R],
    "R2": [R, R],
    "R3": [R, R, R],
    "H": [H],
    "V": [V],
    "RV": [R, V],
    "RH": [R, H]
}

class Tile(object):
    def __init__(self, n, tile):
        self.n = n
        self.tile = np.array(tile)
        self.adj = set()

def solve(data):
    tiles = []
    for tile in data:
        n = int(tile[0].split(" ")[1][:-1])
        body = [list(row) for row in tile[1:] if row]
        tiles.append(Tile(n, body))

    matched = set()
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            a, b = tiles[i], tiles[j]
            if i == j or (a.n, b.n) in matched:
                continue
            for aop, afns in OPS.items():
                aconf = np.array(a.tile)
                for afn in afns:
                    aconf = afn(aconf)
                for bop, bfns in OPS.items():
                    bconf = np.array(b.tile)
                    for bfn in bfns:
                        bconf = bfn(bconf)
                    criteria = [
                        aconf[0] == bconf[len(bconf) - 1],
                        aconf[len(aconf) - 1] == bconf[0],
                        aconf[:, 0] == bconf[:, len(bconf) - 1],
                        aconf[:, len(aconf) - 1] == bconf[:, 0]
                    ]
                    if any(criterion.all() for criterion in criteria):
                        a.adj.add(b.n)
                        b.adj.add(a.n)
                        matched.add((a.n, b.n))
                        break
    
    prod = 1
    for tile in tiles:
        if len(tile.adj) == 2:
            prod *= tile.n
    return prod

def main():
    with open("input/20.txt") as f:
        data = ""
        for line in f:
            data += line
        tiles = [tile.split("\n") for tile in data.split("\n\n")]
        print(solve(tiles))

if __name__ == "__main__":
    main()