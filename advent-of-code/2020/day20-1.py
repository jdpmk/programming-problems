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
