from flask import Flask,render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_points", methods = ["GET"])
def get():
    sql = text("SELECT id, latitude, longitude FROM point")
    result = db.session.execute(sql)
    points = result.fetchall()
    points_data =[{'id': point.id, 'latitude': point.latitude, 'longitude': point.longitude} for point in points]
    return jsonify({"points": points_data})


@app.route("/create_point", methods=["POST"])
def add():
    try:
        data = request.get_json()

        latitude = data.get("latitude")
        longitude = data.get("longitude")

        sql = text("INSERT INTO point (latitude, longitude) VALUES (:latitude, :longitude) RETURNING id")
        result = db.session.execute(sql, {"latitude": latitude, "longitude": longitude})
        db.session.commit()

        point_id = result.fetchone()[0]
        return jsonify({"id": point_id})

    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/point/<int:id>")
def point(id):
    sql = text("SELECT latitude, longitude FROM point WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    point = result.fetchall()
    return render_template("point.html", id = id, point=point)