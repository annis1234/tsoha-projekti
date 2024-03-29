from app import app
import points, users, messages, likes, images
from flask import jsonify, render_template, request, redirect, url_for, session, abort

@app.route("/")
def index():
    count = points.get_count()
    best = points.get_most_popular()
    print(best)
    return render_template("index.html", count=count, best=best)

@app.route("/get_points", methods = ["GET"])
def get_points():
    res= points.get_all()
    points_data =[{'id': point.id, 'latitude': point.latitude, 'longitude': point.longitude, 'title': point.title} for point in res]
    return jsonify({"points": points_data})

@app.route("/point/<int:id>")
def point(id):
    point = points.get_one(id)
    msg = messages.get_messages()
    like_count=likes.get_likes()
    creator = points.get_creator(id)

    return render_template("point.html", id = id, point=point, msg=msg, like_count=like_count, creator = creator)

@app.route("/get_image/<int:id>")
def get_image(id):
    try:
        img =images.get_image(id)
        return img

    except Exception as e:
        return render_template("error_point.html", message=e, id = id)

@app.route("/create_point", methods=["POST"])
def add():
    point_id = points.create_point()
    if point_id:
        return jsonify({"id": point_id})
    
    else:
        return render_template("error.html", message="Pisteen lisäys epäonnistui")
    
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
            error = "Käyttäjätunnuksen luonti epäonnistui"
            return redirect(url_for("new_user", error =error))
            

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        return redirect("/")
    else:
        error = "Virheellinen käyttäjätunnus tai salasana"
        return redirect(url_for("index", error = error))
     
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/send_message", methods=["POST"])
def send_message():

        message = request.form['message']

        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        
        id = points.get_point_id()
        if messages.send_message(message):
            return redirect("/point/{}".format(id))
        
        else:
            return render_template("error_point.html", message="Et voi lähettää viestiä ilman sisältöä!", id = id)
    
@app.route("/delete_point", methods=["DELETE"])
def delete_point():
    try:
        id = points.get_point_id()
        points.delete_point(id)
        return jsonify({"message": "point deleted"})
    except Exception as e:
        return render_template("error_point.html", message="Pisteen poistaminen epäonnistui", id = id)
    
@app.route("/like", methods = {"POST"})
def like():
    id = points.get_point_id()
    l = likes.get_likes()
    try:
        likes.like()
        return redirect("/point/{}".format(id))
    except Exception as e:
        return redirect("/point/{}".format(id))
    

@app.route("/send", methods=["POST"])
def send():
    try:
        id = points.get_point_id()
        file = request.files["file"]
        name = file.filename
        if not name.endswith(".jpg"):
            return "Invalid filename"
        data = file.read()
        if len(data) > 1000*1200:
            return "Too big file"
        else:
            images.send_image(name, data, id)
            return redirect("/point/{}".format(id))
        
    except Exception as e:
        return render_template("error_point.html", message="Kuvan lisäys epäonnistui", id = id)
        
