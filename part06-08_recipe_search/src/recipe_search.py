# Write your solution here
def read_recipes(filename: str):
    recipes = []
    
    with open(filename) as file:
        lines = [line.strip() for line in file]

    i = 0
    while i < len(lines):
        if lines[i] == "":
            i += 1
            continue

        name = lines[i]
        prep_time = int(lines[i+1])
        i += 2

        ingredients = []
        while i < len(lines) and lines[i] != "":
            ingredients.append(lines[i])
            i += 1

        recipes.append((name, prep_time, ingredients))

    return recipes


def search_by_name(filename: str, word: str):
    recipes = read_recipes(filename)
    result = []

    for name, prep_time, ingredients in recipes:
        if word.lower() in name.lower():
            result.append(name)

    return result


def search_by_time(filename: str, prep_time: int):
    recipes = read_recipes(filename)
    result = []

    for name, time, ingredients in recipes:
        if time <= prep_time:
            result.append(f"{name}, preparation time {time} min")

    return result


def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_recipes(filename)
    result = []

    for name, prep_time, ingredients in recipes:
        if ingredient.lower() in [i.lower() for i in ingredients]:
            result.append(f"{name}, preparation time {prep_time} min")

    return result