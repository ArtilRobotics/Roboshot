# drinks_more_recipes.py
from Hector9000.conf import database as DB
drink_list = [
    {
        "name": "Mojito de limón",
        "recipe": [
            ("ingr", "lim", 30),
            ("ingr", "sir_hierba", 30),
            ("ingr", "ron_b", 60),
            ("ingr", "sprite", 120)
        ],
        "image": "../Hector9000/Images/margarita-limon.png"
    },{
        "name": "Mojito de maracuyá",
        "recipe": [
            ("ingr", "mar", 30),
            ("ingr", "sir_hierba", 30),
            ("ingr", "ron_b", 60),
            ("ingr", "sprite", 120)
        ],
        "image": "../Hector9000/Images/mojito-maracuya.png"
    } ,{
        "name": "Daiquiri de limón",
        "recipe": [
            ("ingr", "lim", 30),
            ("ingr", "siro", 30),
            ("ingr", "ron_b", 60),
            ("ingr", "sprite", 120)
        ],
        "image": "../Hector9000/Images/daiquiri-limon.png"
    }, {
        "name": "Daiquiri de maracuyá",
        "recipe": [
            ("ingr", "mar", 30),
            ("ingr", "siro", 30),
            ("ingr", "ron_b", 60),
            ("ingr", "sprite", 120)
        ],
        "image": "../Hector9000/Images/daiquiri-maracuya.png"
    }, {
        "name": "Margarita de limón",
        "recipe": [
            ("ingr", "lim", 60),
            ("ingr", "siro", 30),
            ("ingr", "teq", 90)
        ],
        "image": "../Hector9000/Images/margarita-limon.png"
    }, {
        "name": "Margarita de maracuyá",
        "recipe": [
            ("ingr", "mar", 60),
            ("ingr", "siro", 30),
            ("ingr", "teq", 90)
        ],
        "image": "../Hector9000/Images/mojito.png"
    }, {
        "name": "Tinto de verano",
        "recipe": [
            ("ingr", "lim", 30),
            ("ingr", "nar", 30),
            ("ingr", "vino", 180),
            ("ingr", "sprite", 120) 
        ],
        "image": "../Hector9000/Images/mojito.png"
    }, {
        "name": "Moscow mule",
        "recipe": [
            ("ingr", "lim", 30),
            ("ingr", "nar", 30),
            ("ingr", "sir_pic", 30),
            ("ingr", "vodka", 90), 
            ("ingr", "gin", 180), 
        ],
        "image": "../Hector9000/Images/mojito.png"
    }, {
        "name": "Tequila mule",
        "recipe": [
            ("ingr", "lim", 60),
            ("ingr", "sir_pic", 30),
            ("ingr", "teq", 90),
            ("ingr", "gin", 180)
        ],
        "image": "../Hector9000/Images/mojito.png"
    }, {
        "name": "Margarita jalapeño",
        "recipe": [
            ("ingr", "lim", 60),
            ("ingr", "sir_pic", 60),
            ("ingr", "teq", 90)
        ],
        "image": "../Hector9000/Images/mojito.png"
    }, {
        "name": "Vodka de verano",
        "recipe": [
            ("ingr", "nar", 180),
            ("ingr", "siro", 30),
            ("ingr", "vodka", 60),
            ("ingr", "vino", 60)
        ],
        "image": "../Hector9000/Images/mojito.png"
    }
]


myDB = DB.Database()

available_ingredients = myDB.get_Servos_asList()
ingredients = myDB.get_AllIngredientsAsDict()


# executable
def doable(drink, available): 
    return False not in [ing in available for ing in [step[1]
                                                      for step in drink["recipe"] if step[0] == "ingr"]]


def alcoholic(drink):
    return True in [ingredients[step[1]][1]
                    for step in drink["recipe"] if step[0] == "ingr"]


available_drinks = [
    drink for drink in drink_list if doable(
        drink, available_ingredients)]

