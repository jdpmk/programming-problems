"""
--- Part Two ---
As you look over the list of messages, you realize your matching rules aren't quite right. To fix them, completely replace rules 8: 42 and 11: 42 31 with the following:

8: 42 | 42 8
11: 42 31 | 42 11 31
This small change has a big impact: now, the rules do contain loops, and the list of messages they could hypothetically match is infinite. You'll need to determine how these changes affect which messages are valid.

Fortunately, many of the rules are unaffected by this change; it might help to start by looking at which rules always match the same set of values and how those rules (especially rules 42 and 31) are used by the new versions of rules 8 and 11.

(Remember, you only need to handle the rules you have; building a solution that could handle any hypothetical combination of rules would be significantly more difficult.)

For example:

42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
Without updating rules 8 and 11, these rules only match three messages: bbabbbbaabaabba, ababaaaaaabaaab, and ababaaaaabbbaba.

However, after updating rules 8 and 11, a total of 12 messages match:

bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
After updating rules 8 and 11, how many messages completely match rule 0?
"""

import re

def traverse(g, k, processed):
    if "\"" in g[k]:
        return g[k].strip("\"")
    if processed.get(k, False):
        if k == 8:
            g[k] = traverse(g, 42, processed) + "+"
        if k == 11:
            p1 = traverse(g, 42, processed)
            p2 = traverse(g, 31, processed)
            g[k] = (p1 + "(") * 5 + p1 + p2 + (")*" + p2) * 5
        return g[k]
    processed[k] = True
    options = []
    for seq in g[k]:
        results = []
        for adj in seq:
            results.append(traverse(g, adj, processed))
        options.append("".join([result.replace("^", "").replace("$", "") for result in results]))
    g[k] = "(" + "|".join(["^" + option + "$" for option in options]) + ")"
    return g[k]

def solve(rules, messages):
    g = {}
    for rule in rules:
        no, content = rule.split(": ")
        if no == "8":
            g[int(no)] = "42 | 42 8"
        elif no == "11":
            g[int(no)] = "42 31 | 42 11 31"
        else:
            g[int(no)] = content
    for k, v in g.items():
        if "\"" in v:
            continue
        g[k] = [[int(a) for a in seq.split(" ")] for seq in v.split(" | ")]

    processed = {}
    for k in g.keys():
        if not processed.get(k, False):
            traverse(g, k, processed)

    for k in g.keys():
        if "\"" not in g[k]:
            g[k] = g[k][1:len(g[k]) - 1]
        else:
            g[k] = "^" + g[k].strip("\"") + "$"

    matches = 0
    for message in messages:
        if re.match(g[0], message):
            matches += 1
    
    return matches

def main():
    with open("input/19.txt") as f:
        data = ""
        for line in f:
            data += line
        rules, messages = data.split("\n\n")
        print(solve(rules.split("\n"), messages.split("\n")))

if __name__ == "__main__":
    main()