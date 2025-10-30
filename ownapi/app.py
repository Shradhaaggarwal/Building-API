from flask import Flask, request 
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
db = SQLAlchemy(app); 
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True); 
    name = db.Column(db.String(80), nullable = False, unique = True); 
    desc = db.Column(db.String(200), nullable = False); 

    def __repr__(self):
        return f"Drink {self.name} : {self.desc}"

@app.route('/shradha')
def index():
    return "hello shradha"

@app.route('/drinks')
def drink():

    drinkss = Drink.query.all();
    output = [];
    for drink in drinkss:
        drink_data = {'name': drink.name, 'desc': drink.desc}; 
        output.append(drink_data);

    return {"drink" : output};


@app.route('/drinks/<id>')
def drink_by_id(id):

    drink = Drink.query.get_or_404(id); #table wala DRINK
    return {"name": drink.name, "desc": drink.desc}; 


@app.route('/drinks', methods=['POST'])
def add_drink():
    dd = Drink(name = request.json['name'], desc = request.json['desc']);
    db.session.add(dd);
    db.session.commit();
    return {"id": dd.id};

@app.route('/drink/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get_or_404(id);
    if drink is None:
        return {"message": "drink not found"}, 404
    db.session.delete(drink);
    db.session.commit();
    return {"message": "deleted successfully"};

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)

