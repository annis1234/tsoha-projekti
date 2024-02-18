from app import app
import points, users, messages
from flask import jsonify, render_template, request, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_points", methods = ["GET"])
def get_points():
    res= points.get_all()
    points_data =[{'id': point.id, 'latitude': point.latitude, 'longitude': point.longitude, 'title': point.title} for point in res]
    return jsonify({"points": points_data})

@app.route("/point/<int:id>")
def point(id):
    point = points.get_one(id)
    msg = messages.get_messages()
    return render_template("point.html", id = id, point=point, msg=msg)

@app.route("/create_point", methods=["POST"])
def add():
    try:
        point_id = points.create_point()
        return jsonify({"id": point_id})
    except Exception as e:
        return render_template("error.html", message=e)
    
@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/create_user", methods=["POST"])
def create_user():
        username = request.form["username"]
        password = request.form["password"]

        if users.create_user(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Käyttäjätunnuksen luonti epäonnistui")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        return redirect("/")
    else:
        return render_template("error.html", message="väärä käyttäjätunnus tai salasana")
    
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/send_message", methods=["POST"])
def send_message():

    try:
        message = request.form['message']
        id = points.get_point_id()
        point = points.get_one(id)
        msg = messages.get_messages()
        if messages.send_message(message):
            return render_template("point.html", id = id, point=point, msg=msg, new=message)
        
    except Exception as e:
        return {"message": str(e)}
    
@app.route("/delete_point", methods=["DELETE"])
def delete_point():
    id = points.get_point_id()
    try:
        points.delete_point(id)
        return jsonify({"message": "point deleted"})
    except Exception as e:
        return {"message":  str(e)}
        
