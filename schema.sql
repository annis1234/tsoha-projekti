CREATE TABLE points 
    (id SERIAL PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT,
    title TEXT, description TEXT);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT, password TEXT);
