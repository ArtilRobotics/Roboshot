# drinks_more_recipes.py
from Hector9000.conf import database as DB
drink_list = [
    {
        "name": "Piña colada",
        "recipe": [
            ("ingr", "rum", 50),
        ],
        "image": "../Hector9000/Images/pina-colada.png"
    },{
        "name": "Margarita frozen de fresa",
        "recipe": [
            ("ingr", "gin", 60),
            ("ingr", "gibe", 50),
        ],
        "image": "../Hector9000/Images/margarita-fresa.png"
    } ,{
        "name": "Margarita frozen de limón",
        "recipe": [
            ("ingr", "tonic", 35),
            ("ingr", "gga", 40),
            ("ingr", "oj", 110),
        ],
        "image": "../Hector9000/Images/margarita-frozen.png"
    }, {
        "name": "Pisco Sunrise",
        "color": "white",
        "recipe": [
            ("ingr", "gin", 40),
            ("ingr", "tonic", 120),
        ],
        "image": "../Hector9000/Images/pisco-sunrise.png"
    }, {
        "name": "Cosmopolitan",
        "color": "orange",
        "recipe": [
            ("ingr", "vodka", 40),
            ("ingr", "oj", 120),
            ("ingr", "rum", 50),
            ("ingr", "gibe", 70),
            ("stir", True),
        ],
        "image": "../Hector9000/Images/cosmopolitan.png"
    }, {
        "name": "Mojito",
        "color": "red",
        "recipe": [
            ("ingr", "oj", 140),
            ("ingr", "gren", 15),
            ("umb", True),
        ],
        "image": "../Hector9000/Images/mojito.png"
    }
]


myDB = DB.Database()

available_ingredients = myDB.get_Servos_asList()
ingredients = myDB.get_AllIngredientsAsDict()


def doable(drink, available):
    return False not in [ing in available for ing in [step[1]
                                                      for step in drink["recipe"] if step[0] == "ingr"]]


def alcoholic(drink):
    return True in [ingredients[step[1]][1]
                    for step in drink["recipe"] if step[0] == "ingr"]


available_drinks = [
    drink for drink in drink_list if doable(
        drink, available_ingredients)]

