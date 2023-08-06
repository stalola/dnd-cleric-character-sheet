CREATE TABLE characters (
id SERIAL PRIMARY KEY, 
user_id INTEGER REFERENCES users, 
character_name TEXT,
speed INTEGER,
race TEXT, 
level INTEGER,
strength INTEGER,
dexterity INTEGER,
constitution INTEGER,
intelligence INTEGER,
wisdom INTEGER,
charisma INTEGER
);

CREATE TABLE users (
id SERIAL PRIMARY KEY,
username TEXT,
password TEXT
);