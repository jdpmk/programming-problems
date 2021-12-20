import copy
import math

def enhance(algorithm, pixels, imin, imax, jmin, jmax, border):
    pixels_ = copy.deepcopy(pixels)

    for i in range(imin - 1, imax + 2):
        pixels_[i] = pixels_.get(i, {})
        for j in range(jmin - 1, jmax + 2):
            idx = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    idx = idx * 2 + pixels.get(i + di, {}).get(j + dj, border)

            pixels_[i][j] = algorithm[idx] == '#'

    return pixels_

def solve(algorithm, img):
    imin, imax = math.inf, -math.inf
    jmin, jmax = math.inf, -math.inf

    pixels = {}

    for i, row in enumerate(img):
        pixels[i] = pixels.get(i, {})
        for j, pixel in enumerate(row):
            if pixel == '#':
                imin = min(imin, i)
                imax = max(imax, i)
                jmin = min(jmin, j)
                jmax = max(jmax, j)
                pixels[i][j] = True
            else:
                pixels[i][j] = False

    num_iterations = 50
    for step in range(num_iterations):
        pixels = enhance(algorithm, pixels,
                         imin, imax, jmin, jmax,
                         step % 2 if algorithm[0] == '#' != algorithm[-1] else False)
        imin, imax, jmin, jmax = imin - 1, imax + 1, jmin - 1, jmax + 1

    ct = 0
    for i in range(imin, imax + 1):
        pixels[i] = pixels.get(i, {})
        for j in range(jmin, jmax + 1):
            ct += pixels.get(i, {}).get(j, False)

    return ct

def main():
    with open("input/20.data") as f:
        algorithm = f.readline().strip()
        f.readline()
        img = [line.strip() for line in f.readlines()]
        print(solve(algorithm, img))

if __name__ == "__main__":
    main()
