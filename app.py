from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from models import db, Bird

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://kelly985:eDR0rSVwVPYTnIlQLcPipEFDn7haHxl2@dpg-cjit0e0cfp5c73aqdlfg-a.ohio-postgres.render.com/birds_db_22cs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/birds', methods=['GET'])
def get_birds():
    birds = [bird.to_dict() for bird in Bird.query.all()]
    return make_response(jsonify(birds), 200)

@app.route('/add-bird/name/species', methods=['POST'])
def add_bird(name, species):
    # data = request.json
    # name = data.get('name')
    # species = data.get('species')

    # if not name or not species:
    #     return make_response(jsonify({'error': 'Name and species are required fields'}), 400)

    bird = Bird(name=name, species=species)
    db.session.add(Bird)
    db.session.commit()

    return make_response(jsonify({'message': 'Bird added successfully'}), 201)

if __name__ == '__main__':
    app.run(debug=True)
