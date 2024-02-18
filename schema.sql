CREATE TABLE points 
    (id SERIAL PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT,
    title TEXT,
    description TEXT);

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
