from db import db
from flask import request, session
from sqlalchemy.sql import text
import users, points

def get_messages():
    point_id = points.get_point_id()
    sql = text("SELECT content, sent_at, username FROM messages LEFT JOIN users ON messages.user_id = users.id WHERE point_id=:point_id")
    result = db.session.execute(sql,{"point_id": point_id})
    return result.fetchall()

def send_message(message):
    user_id = users.get_user()
    point_id = points.get_point_id()
    content = message
    sql = text("INSERT INTO messages (content, user_id, point_id, sent_at) VALUES (:content, :user_id, :point_id, NOW())")
    result = db.session.execute(sql, {"content": content, "user_id": user_id, "point_id" : point_id})
    db.session.commit()
    return result

