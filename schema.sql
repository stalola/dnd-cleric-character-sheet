CREATE TABLE users (
id SERIAL PRIMARY KEY,
username TEXT UNIQUE,
password TEXT
CONSTRAINT check_no_space CHECK (username NOT LIKE '% %')
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

CREATE TABLE spells (
id SERIAL PRIMARY KEY,
name TEXT,
level INTEGER,
cast_time TEXT, 
duration TEXT, 
range_area TEXT, 
components TEXT, 
school TEXT, 
attack_save TEXT, 
damage_effect TEXT, 
description TEXT
);

CREATE TABLE spellbook (
id SERIAL PRIMARY KEY,
spell_id INTEGER REFERENCES spells,
char_id INTEGER REFERENCES characters,
prepared BOOL
);