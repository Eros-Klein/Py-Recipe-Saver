import model.recipe as recipe

def polluteExampleData(db):
    recipe.recipe('Pizza', 'Bake it', ['Dough', 'Tomato Sauce', 'Cheese'], db)
    recipe.recipe('Pasta', 'Boil it', ['Pasta', 'Tomato Sauce', 'Cheese'], db)
    recipe.recipe('Salad', 'Mix it', ['Lettuce', 'Tomato', 'Cucumber'], db)