import flask as fl
import example.demo as demo

from db.postgre import db

database = db()
app = fl.Flask(__name__)

demo.polluteExampleData(database)

@app.route('/')
def index():
    return fl.jsonify([recipe.to_dict() for recipe in database.get_all_recipes()])

app.run(port=5000)