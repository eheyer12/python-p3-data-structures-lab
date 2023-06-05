spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    heat = [food for food in spicy_foods if food["heat_level"] > 5]
    return heat


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if food['cuisine'] == cuisine][0]

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
        else:
            pass

def get_average_heat_level(spicy_foods):
    pass
    heat_level = [food['heat_level'] for food in spicy_foods]
    return sum(heat_level) / len(heat_level)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
