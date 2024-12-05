class recipe_interface:
    id: int
    name: str
    instructions: str
    ingredients: list[str]
    
    def __init__(self, id: int, name: str, instructions: str, ingredients: list[str]):
        self.id = id
        self.name = name
        self.instructions = instructions
        self.ingredients = ingredients
        
    def __str__(self):
        return f'{self.name} - {self.instructions} - {self.ingredients}'
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "instructions": self.instructions,
            "ingredients": self.ingredients,
        }
    
class recipe_dto:
    id: int
    name: str
    instructions: str
    
    def __init__(self, id: int, name: str, instructions: str):
        self.id = id
        self.name = name
        self.instructions = instructions
        

class ingredient_dto:
    id: int
    name: str
    recipe_id: int
    
    def __init__(self, id: int, name: str, recipe_id: int):
        self.id = id
        self.name = name
        self.recipe_id = recipe_id