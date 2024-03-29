from db import db
from flask import request, session
from sqlalchemy.sql import text


def get_all():
    sql = text("SELECT id, latitude, longitude, title FROM points")
    result = db.session.execute(sql)
    return result.fetchall()

def get_one(id):
    sql = text("SELECT latitude, longitude, title, description FROM points WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    session["point_id"] = id
    return result.fetchall()

def create_point():
    data = request.get_json()

    latitude = data.get("latitude")
    longitude = data.get("longitude")
    title = data.get("title")
    description = data.get("description")

    creator = session.get('user_id')

    if not title or not description:
        return False
    
    elif len(title) > 20 or len(description) > 5000:
        return False

    sql = text("INSERT INTO points (latitude, longitude, title, description, user_id) VALUES (:latitude, :longitude, :title, :description, :user_id) RETURNING id")
    result = db.session.execute(sql, {"latitude": latitude, "longitude": longitude, "title": title, "description": description, "user_id": creator})
    db.session.commit()

    return result.fetchone()[0]

def get_point_id():
    return session.get("point_id", 0)

def delete_point(id):
    sql = text("DELETE FROM Points WHERE id=:id")
    db.session.execute(sql, {"id":id})
    db.session.commit()

def get_count():
    sql = text("SELECT COUNT(*) from POINTS")

    result = db.session.execute(sql)

    return result.fetchone()[0]

def get_most_popular():
    sql = text("SELECT points.id, title, latitude, longitude, COUNT(points.id) FROM points \
               LEFT JOIN likes ON points.id = likes.point_id GROUP BY points.id ORDER BY COUNT(points.id) DESC LIMIT 5")

    result = db.session.execute(sql)
    
    return result.fetchall()

def get_coordinates(id):
    sql = text ("SELECT latitude, longitude FROM points WHERE id =:id")
    result = db.session.execute(sql, {"id": id})
    return result.fetchall()

def get_creator(point_id):
    sql = text("SELECT username FROM users LEFT JOIN points ON points.user_id = users.id WHERE points.id=:id")
    result = db.session.execute(sql, {"id": point_id})
    return result.fetchone()[0]