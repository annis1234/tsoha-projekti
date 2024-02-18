from db import db
from flask import make_response
from sqlalchemy.sql import text
import points

def get_image(id):
    sql = text("SELECT data FROM images WHERE point_id=:point_id")
    result = db.session.execute(sql, {"point_id": id})
    data = result.fetchone()[0]
    if data:
        res = make_response(bytes(data))
        res.headers.set("Content-Type", "image/jpeg")
        return res

def send_image(name, data, point_id):
    sql = text("INSERT INTO images (name,data, point_id) VALUES (:name,:data, :point_id)")
    db.session.execute(sql, {"name":name, "data":data, "point_id": point_id})
    db.session.commit()
