# drinks_more_recipes.py
from Hector9000.conf import database as DB
drink_list = [
    {
        "name": "Piña colada",
        "recipe": [("ingr", "mate", 50)],
        "image": "https://www.elcolombiano.com/binrepository/470x604/0c19/470d565/none/11101/QXGP/bad-bunny-concierto-instagram_40231022_20220630145812.jpg"
    },{
        "name": "Margarita frozen de fresa",
        "recipe": [
            ("ingr", "vodka", 60),
            ("ingr", "lime", 10),
            ("ingr", "gibe", 180),
        ],
        "image": "https://www.pngfind.com/pngs/m/626-6261425_margarita-de-fresa-coctel-margarita-de-fresa-hd.png"
    } ,{
        "name": "Margarita frozen de limón",
        "recipe": [
            ("ingr", "vodka", 60),
            ("ingr", "lime", 10),
            ("ingr", "gibe", 180),
        ],
        "image": "https://w7.pngwing.com/pngs/421/515/png-transparent-margarita-cocktail-slush-fizzy-drinks-liqueur-tangy-food-recipe-non-alcoholic-beverage-thumbnail.png"
    }, {
        "name": "Pisco Sunrise",
        "color": "white",
        "recipe": [
            ("ingr", "gin", 40),
            ("ingr", "tonic", 120),
        ],
        "image": "https://e7.pngegg.com/pngimages/885/148/png-clipart-tequila-sunrise-cocktail-margarita-sangria-cocktail-food-recipe-thumbnail.png"
    }, {
        "name": "Cosmopolitan",
        "color": "orange",
        "recipe": [
            ("ingr", "vodka", 40),
            ("ingr", "oj", 120),
            ("stir", True),
        ],
        "image": "https://img2.freepng.es/20180622/xqq/kisspng-cosmopolitan-cocktail-martini-soju-vodka-5b2d1a8ba8fcd5.3191597715296825716922.jpg"
    }, {
        "name": "Mojito",
        "color": "red",
        "recipe": [
            ("ingr", "oj", 140),
            ("ingr", "gren", 15),
            ("umb", True),
        ],
        "image": "https://img2.freepng.es/20180403/cfe/kisspng-mojito-cocktail-juice-fizzy-drinks-beer-mojito-5ac3d281e8f5d1.7511593015227828499542.jpg"
    }
]

actions = {
    # code      text     is_automatic?
    "ingr": ("Add Ingredient", True),
    "ping": ("Ring Bell", True),
    "shake": ("Shake", False),
    "stir": ("Stir", False),
    "ice": ("Add Ice", False),
    "umb": ("Add Umbrella", False),
}


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
