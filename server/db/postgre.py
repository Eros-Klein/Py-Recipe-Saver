import psycopg2
import model.interfaces as interfaces

class db:
    conn = psycopg2.connect(
            database='recipe_db',
            user='admin',
            password='recipe',
            host='localhost',
            port='5432',
        )
    cur = conn.cursor()
    
    def __init__(self):
        # Only Execute if you changed the schema (Resets the DB)
        self.cur.execute('DROP TABLE IF EXISTS ingredients')
        self.cur.execute('DROP TABLE IF EXISTS recipes')
        
        self.cur.execute('CREATE TABLE IF NOT EXISTS recipes (id SERIAL PRIMARY KEY, name TEXT, instructions TEXT)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS ingredients (id SERIAL PRIMARY KEY, name TEXT, recipe_id INTEGER, FOREIGN KEY(recipe_id) REFERENCES recipes(id))')
        
    # TODO: Mind that the name should not be unique in the final version
    def insert(self, recipe: interfaces.recipe_interface):
        self.cur.execute('INSERT INTO recipes (name, instructions) VALUES (%s, %s) RETURNING id', (recipe.name, recipe.instructions))
        id = self.cur.fetchone()[0]
        
        for ingredient in recipe.ingredients:
            self.cur.execute('INSERT INTO ingredients (name, recipe_id) VALUES (%s, %s)', (ingredient, id))
            
        self.conn.commit()
        return id
        
    # TODO: The mapping in this function is not the cleanest. If you find a better way, please change it.
    def get_all_recipes(self):
        self.cur.execute('SELECT * FROM recipes')
        recipes: list[interfaces.recipe_dto] = [interfaces.recipe_dto(recipe[0], recipe[1], recipe[2]) for recipe in self.cur.fetchall()]
        self.cur.execute('SELECT * FROM ingredients')
        ingredients: list[interfaces.ingredient_dto] = [interfaces.ingredient_dto(ingredient[0], ingredient[1], ingredient[2]) for ingredient in self.cur.fetchall()]
        full_recipes = [interfaces.recipe_interface(id=recipe.id, name=recipe.name, instructions=recipe.instructions, ingredients=[ingredient.name for ingredient in ingredients if ingredient.recipe_id == recipe.id]) for recipe in recipes]
        return full_recipes
    
    def shutdown(self):
        self.cur.close()
        self.conn.close()