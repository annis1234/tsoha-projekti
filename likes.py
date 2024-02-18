from db import db
from flask import request, session
from sqlalchemy.sql import text
import users, points

def get_likes():

    point_id = points.get_point_id()
    sql = text("SELECT count FROM likes WHERE point_id=:point_id")
    result = db.session.execute(sql, {"point_id": point_id}).fetchone()

    if result is None:
        likes = 0
    else:
        likes = result[0]
    return likes

def like():
    point_id = points.get_point_id()
    sql = text("SELECT count FROM likes WHERE point_id=:point_id")
 
    likes = db.session.execute(sql, {"point_id": point_id})

    result = likes.fetchall()

    if not result:
        sql = text("INSERT INTO likes (point_id, count) VALUES (:point_id, :count)")
        db.session.execute(sql, {"point_id": point_id, "count": 1})
        db.session.commit()

    else:
        sql = text("UPDATE likes SET count = count+1 WHERE point_id=:point_id")
        db.session.execute(sql, {"point_id": point_id})
        db.session.commit()