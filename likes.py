from db import db
from flask import request, session
from sqlalchemy.sql import text
import users, points

def get_likes():

    point_id = points.get_point_id()
    sql = text("SELECT COUNT(*) FROM likes WHERE point_id=:point_id")
    result = db.session.execute(sql, {"point_id": point_id}).fetchone()

    if result is None:
        likes = 0
    else:
        likes = result[0]
    return likes

def like():
    user_id = users.get_user()
    point_id = points.get_point_id()

    sql = text("INSERT INTO likes (point_id, count, user_id) VALUES (:point_id, :count, :user_id)")

    db.session.execute(sql, {"point_id": point_id, "count": 1, "user_id": user_id})
    db.session.commit()