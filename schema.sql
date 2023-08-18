CREATE TABLE users (
id SERIAL PRIMARY KEY,
username TEXT,
password TEXT
);

CREATE TABLE characters (
id SERIAL PRIMARY KEY, 
user_id INTEGER REFERENCES users, 
character_name TEXT,
race TEXT,
speed INTEGER,
level INTEGER,
strength INTEGER,
dexterity INTEGER,
constitution INTEGER,
intelligence INTEGER,
wisdom INTEGER,
charisma INTEGER,
acrobatics INTEGER GENERATED ALWAYS AS ((dexterity - 10)/2) STORED,
animal_handling INTEGER GENERATED ALWAYS AS ((wisdom - 10)/2) STORED,
arcana INTEGER GENERATED ALWAYS AS ((intelligence - 10)/2) STORED,
athletics INTEGER GENERATED ALWAYS AS ((strength - 10)/2) STORED,
deception INTEGER GENERATED ALWAYS AS ((charisma - 10)/2) STORED,
history INTEGER GENERATED ALWAYS AS ((intelligence - 10)/2) STORED,
insight INTEGER GENERATED ALWAYS AS ((wisdom - 10)/2) STORED,
intimidation INTEGER GENERATED ALWAYS AS ((charisma - 10)/2) STORED,
investigation INTEGER GENERATED ALWAYS AS ((intelligence - 10)/2) STORED,
medicine INTEGER GENERATED ALWAYS AS ((wisdom - 10)/2) STORED,
nature INTEGER GENERATED ALWAYS AS ((intelligence - 10)/2) STORED,
perception INTEGER GENERATED ALWAYS AS ((wisdom - 10)/2) STORED,
performance INTEGER GENERATED ALWAYS AS ((charisma - 10)/2) STORED,
persuasion INTEGER GENERATED ALWAYS AS ((charisma - 10)/2) STORED,
religion INTEGER GENERATED ALWAYS AS ((intelligence - 10)/2) STORED,
sleight_of_hand INTEGER GENERATED ALWAYS AS ((dexterity - 10)/2) STORED,
stealth INTEGER GENERATED ALWAYS AS ((dexterity - 10)/2) STORED,
survival INTEGER GENERATED ALWAYS AS ((wisdom - 10)/2) STORED
);