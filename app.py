from flask import Flask,render_template, request, jsonify, session, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key=getenv("SECRET_KEY")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/create_user", methods=["POST"])
def create():
    try: 
        username = request.form["username"]
        password = request.form["password"]

        hash_value = generate_password_hash(password)
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
        session["username"] = username
        return redirect("/")

    except Exception as e:
        return jsonify({"error": str(e)})
    

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = text("SELECT id, password FROM users WHERE username =:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()

    if not user:
        return jsonify("username does not exist")
    
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username
            return redirect("/")
        else:
            return jsonify("wrong username or password")
        
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/get_points", methods = ["GET"])
def get():
    sql = text("SELECT id, latitude, longitude, title FROM points")
    result = db.session.execute(sql)
    points = result.fetchall()
    points_data =[{'id': point.id, 'latitude': point.latitude, 'longitude': point.longitude, 'title': point.title} for point in points]
    return jsonify({"points": points_data})


@app.route("/create_point", methods=["POST"])
def add():
    try:
        data = request.get_json()

        latitude = data.get("latitude")
        longitude = data.get("longitude")
        title = data.get("title")
        description = data.get("description")

        sql = text("INSERT INTO points (latitude, longitude, title, description) VALUES (:latitude, :longitude, :title, :description) RETURNING id")
        result = db.session.execute(sql, {"latitude": latitude, "longitude": longitude, "title": title, "description": description})
        db.session.commit()

        point_id = result.fetchone()[0]
        return jsonify({"id": point_id})

    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route("/point/<int:id>")
def point(id):
    sql = text("SELECT latitude, longitude, title, description FROM points WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    point = result.fetchall()
    return render_template("point.html", id = id, point=point)

@app.route("/send_message", methods=["POST"])
def send_message():
    user_id = session.get("user_id", 0)
    content = request.form['message']
    print(content)
    sql = text("INSERT INTO messages (content, user_id, point_id, sent_at) VALUES (:content, :user_id, :point_id, NOW())")

    db.session.execute(sql, {"content": content, "user_id": user_id})