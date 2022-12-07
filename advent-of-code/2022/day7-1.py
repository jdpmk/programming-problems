FS_ROOT = "/"
FS_PAR  = ".."

CMD    = "$"
CMD_CD = "cd"

MAX_SIZE      = 100000
TOTAL_SIZE    = 70000000
REQUIRED_SIZE = 30000000

DIR = "dir"

def calc_rec_sz(d, fs, sz, rec_sz):
    my_sz = sz.get(d, 0)

    for chd in fs.get(d, []):
        my_sz += calc_rec_sz(chd, fs, sz, rec_sz)

    rec_sz[d] = my_sz
    return my_sz

def solve(lines):
    fs = {}
    sz = {}
    st = []

    for line in lines:
        cwd = FS_ROOT if not st else (FS_ROOT + FS_ROOT.join(st))
        if line[0] == CMD:
            if line[1] == CMD_CD:
                if line[2] == FS_ROOT:
                    st.clear()
                elif line[2] == FS_PAR:
                    st.pop()
                else:
                    st.append(line[2])
        elif line[0] == DIR:
            d = (cwd if cwd == FS_ROOT else (cwd + FS_ROOT)) + line[1]
            fs[cwd] = fs.get(cwd, []) + [d]
        else:
            sz[cwd] = sz.get(cwd, 0) + int(line[0])

    rec_sz = {}
    calc_rec_sz(FS_ROOT, fs, sz, rec_sz)

    return sum(s for _, s in rec_sz.items() if s <= MAX_SIZE)

def main():
    with open("input/7.data") as f:
        lines = [line.strip().split() for line in f.readlines()]
        print(solve(lines))

if __name__ == "__main__":
    main()
