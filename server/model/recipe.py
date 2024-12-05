import model.interfaces as interfaces

# A simplification for database insertation
class recipe(interfaces.recipe_interface):
    def __init__(self, name: str, instructions: str, ingredients: list[str], database):
        self.name = name
        self.instructions = instructions
        self.ingredients = ingredients
        self.id = database.insert(self)