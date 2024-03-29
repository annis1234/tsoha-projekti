CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE, 
    password TEXT);

CREATE TABLE points (
    id SERIAL PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT,
    title TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    user_id INTEGER REFERENCES users
    );

CREATE TABLE  messages(
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    user_id INTEGER REFERENCES users,
    point_id INTEGER REFERENCES points ON DELETE CASCADE,
    sent_at TIMESTAMP
);

CREATE TABLE likes(
    id SERIAL PRIMARY KEY,
    count INTEGER,
    point_id INTEGER REFERENCES points ON DELETE CASCADE,
    user_id INTEGER REFERENCES users,
    UNIQUE(point_id, user_id)

);

CREATE TABLE images(
    id SERIAL PRIMARY KEY,
    name TEXT,
    data BYTEA,
    point_id INTEGER REFERENCES points ON DELETE CASCADE
);
