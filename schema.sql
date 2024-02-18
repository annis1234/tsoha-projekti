CREATE TABLE points (
    id SERIAL PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT,
    title TEXT,
    description TEXT
    );

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT, password TEXT);

CREATE TABLE  messages(
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    point_id INTEGER REFERENCES points ON DELETE CASCADE,
    sent_at TIMESTAMP
);

CREATE TABLE likes(
    id SERIAL PRIMARY KEY,
    count INTEGER,
    point_id INTEGER REFERENCES points ON DELETE CASCADE

);

CREATE TABLE images(
    id SERIAL PRIMARY KEY,
    name TEXT,
    data BYTEA,
    point_id INTEGER REFERENCES points ON DELETE CASCADE
);
