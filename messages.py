from db import db
from flask import request
from sqlalchemy.sql import text
import users, points

def send_message(message):
    user_id = users.get_user()
    point_id = points.get_point_id()
    content = message
    sql = text("INSERT INTO messages (content, user_id, point_id, sent_at) VALUES (:content, :user_id, :point_id, NOW())")
    db.session.execute(sql, {"content": content, "user_id": user_id, "point_id" : point_id})
    db.session.commit()
    return True

