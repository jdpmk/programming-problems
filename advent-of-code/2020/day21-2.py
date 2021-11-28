"""
--- Part Two ---
Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.

In the above example:

    mxmxvkd contains dairy.
    sqjhc contains fish.
    fvjkl contains soy.
    Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.

    Time to stock your raft with supplies. What is your canonical dangerous ingredient list?
"""

def solve(data):
    g = {}
    for line in data:
        ingredients, allergens = line.split(" (contains ")
        ingredients = ingredients.split(" ")
        allergens = allergens[:-2].split(", ")
        for allergen in allergens:
            if allergen not in g:
                g[allergen] = ingredients
            else:
                already_in = g[allergen]
                good = set()
                for existing_ingredient in already_in:
                    if existing_ingredient in ingredients:
                        good.add(existing_ingredient)
                g[allergen] = list(good)

    used = set()
    final = {}
    while True:
        removed = False
        for allergen, ingredients in g.items():
            num_unused = 0
            for ingredient in ingredients:
                if ingredient not in used:
                    num_unused += 1
            if num_unused == 1:
                removed = True
                final[allergen] = ingredients[0]
                used.add(ingredients[0])
                ingredients.remove(ingredients[0])
        if not removed:
            break
    
    ordered = []
    order = sorted(final)
    for allergen in order:
        ordered.append(final[allergen])

    return ",".join(ordered)

def main():
    with open("input/21.txt") as f:
        data = []
        for line in f:
            data.append(line)
        print(solve(data))

if __name__ == "__main__":
    main()
