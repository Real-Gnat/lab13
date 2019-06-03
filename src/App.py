from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from src.Main import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://ioter:iotpassword@localhost/iot-test-db'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SportBuilding(db.Model):
    __tablename__ = 'SportBuildings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=80))
    location = db.Column(db.String(length=80))
    construction_year = db.Column(db.Integer)
    viewers_number = db.Column(db.Integer)

    def __init__(self, name="", location="", construction_year=0, viewers_number=0):
        self.name = name
        self.location = location
        self.construction_year = construction_year
        self.viewers_number = viewers_number

    def __str__(self):
        return "{" + "name='" + str(self.name) + '\'' \
               + ", location='" + str(self.location) + '\'' \
               + ", construction_year=" + str(self.construction_year) \
               + ", viewers_number=" + str(self.viewers_number) + "}"


class SportBuildingSchema(ma.Schema):
    class Meta:
        fields = ('name', 'location', 'construction_year', 'viewers_number')


sport_building_schema = SportBuildingSchema()
sport_buildings_schema = SportBuildingSchema(many=True)
db.create_all()


@app.route("/sportBuildings", methods=["POST"])
def add_sport_building():
    name = request.get_json()["name"]
    location = request.get_json()["location"]
    construction_year = request.get_json()["construction_year"]
    viewers_number = request.get_json()["viewers_number"]

    new_sport_building = SportBuilding(name, location, construction_year, viewers_number)

    db.session.add(new_sport_building)
    db.session.commit()

    return jsonify(request.json)


@app.route("/sportBuildings", methods=["GET"])
def get_sport_buildings():
    all_sport_buildings = SportBuilding.query.all()
    result = sport_buildings_schema.dump(all_sport_buildings)
    return jsonify(result.data)


@app.route("/sportBuildings/<id>", methods=["GET"])
def get_sport_building_by_id(id):
    sport_building = SportBuilding.query.get(id)
    return sport_building_schema.jsonify(sport_building)


@app.route("/sportBuildings/<id>", methods=["PUT"])
def update_sport_building(id):
    sport_building = SportBuilding.query.get(id)

    sport_building.name = request.json["name"]
    sport_building.location = request.json["location"]
    sport_building.construction_year = request.json["construction_year"]
    sport_building.viewers_number = request.json["viewers_number"]

    db.session.commit()
    return sport_building_schema.jsonify(request.json)


@app.route("/sportBuildings/<id>", methods=["DELETE"])
def delete_sport_building(id):
    sport_building = SportBuilding.query.get(id)

    db.session.delete(sport_building)
    db.session.commit()

    return sport_building_schema.jsonify(sport_building)


if __name__ == '__main__':
    app.run(debug=True)
