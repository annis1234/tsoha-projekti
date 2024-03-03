from db import db
from flask import session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash, secrets

def create_user(username, password):

    hash_value = generate_password_hash(password)

    try:
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()

    except:
        return False
    return login(username, password)

def login(username, password):
    
    try:
        sql = text("SELECT id, password FROM users WHERE username =:username")
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()

        if not user:
            return False
    
        else:
            if check_password_hash(user.password, password):
                session["username"] = username
                session["user_id"] = user.id
                session["csrf_token"] = secrets.token_hex(16)
                return True
            else:
                return False
    except:
        return False
    
def get_user():
    return session.get("user_id", 0)

def logout():
    del session["username"]