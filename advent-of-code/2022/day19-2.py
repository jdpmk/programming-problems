import sys

def log(s, *format_args):
    print(s.format(*format_args), file=sys.stderr)

def simulate(blueprint):
    o, c, obo, obc, go, gob = blueprint
    moc = max(o, c, obo, go)
    mcc = obc
    mobc = gob

    def helper(t, nom, ncm, nobm, ngm, no, nc, nob, ng, seen={}):
        if t == 0:
            return ng

        key = (t, nom, ncm, nobm, ngm, no, nc, nob, ng)
        if key in seen:
            return seen[key]

        no_, nc_, nob_, ng_ = no + nom, nc + ncm, nob + nobm, ng + ngm
        best = 0

        if no >= go and nob >= gob:
            best = max(best, helper(t - 1, nom, ncm, nobm, ngm + 1, no_ - go, nc_, nob_ - gob, ng_, seen))

        elif no >= obo and nc >= obc and nobm < mobc:
            best = max(best, helper(t - 1, nom, ncm, nobm + 1, ngm, no_ - obo, nc_ - obc, nob_, ng_, seen))

        else:
            if no >= c and ncm < mcc:
                best = max(best, helper(t - 1, nom, ncm + 1, nobm, ngm, no_ - c, nc_, nob_, ng_, seen))

            if no >= o and nom < moc:
                best = max(best, helper(t - 1, nom + 1, ncm, nobm, ngm, no_ - o, nc_, nob_, ng_, seen))

            best = max(best, helper(t - 1, nom, ncm, nobm, ngm, no_, nc_, nob_, ng_, seen))

        seen[key] = best
        return best

    return helper(32, 1, 0, 0, 0, 0, 0, 0, 0, {})

def solve(blueprints):
    product = 1
    for i, blueprint in enumerate(blueprints[:3]):
        log("Simulating blueprint {}", i + 1)
        product *= simulate(blueprint)
    return product

def main():
    with open("input/19.data") as f:
        blueprint_tokens = [line.strip().split() for line in f.readlines()]
        blueprints = [(int(tokens[6]),
                       int(tokens[12]),
                       int(tokens[18]),
                       int(tokens[21]),
                       int(tokens[27]),
                       int(tokens[30])) for tokens in blueprint_tokens]
        print(solve(blueprints))

if __name__ == "__main__":
    main()
