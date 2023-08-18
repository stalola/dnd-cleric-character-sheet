from sqlalchemy.sql import text
from db import db
import users

def create(character_name, speed, race, level, wisdom, strength, charisma, dexterity, constitution,
           intelligence):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = """INSERT INTO characters(user_id, character_name, race, speed, level, strength, dexterity, constitution, intelligence, wisdom, charisma)
          VALUES (:user_id, :character_name, :race, :speed, :level, :strength, :dexterity, :constitution, :intelligence, :wisdom, :charisma)"""
    db.session.execute(text(sql), {"user_id":user_id, "character_name":character_name, "race":race, "speed":speed, "level":level, "strength":strength,
                                   "dexterity":dexterity, "constitution":constitution, "intelligence":intelligence, "wisdom":wisdom, "charisma":charisma})
    db.session.commit()
    return True

def update(char_id, speed, level, wisdom, strength, charisma, dexterity, constitution,
           intelligence):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = """UPDATE characters 
    SET speed=:speed, level=:level, wisdom=:wisdom, strength=:strength, charisma=:charisma, dexterity=:dexterity, constitution=:constitution, intelligence=:intelligence
    WHERE id=:id"""
    db.session.execute(text(sql), {"id":char_id, "user_id":user_id, "speed":speed, "level":level, "strength":strength,
                                   "dexterity":dexterity, "constitution":constitution, "intelligence":intelligence, "wisdom":wisdom, "charisma":charisma})
    db.session.commit()
    return True

def get_characters():
    user_id = users.user_id()
    sql = """SELECT C.id AS char_id, C.user_id, C.character_name, C.speed, C.race, C.level, C.strength, C.dexterity, C.constitution, C.intelligence, C.wisdom, C.charisma, U.username 
          FROM characters C JOIN users U 
          ON C.user_id=U.id 
          WHERE C.user_id=:user_id"""
    # is it necessary to get all these variables?
    result = db.session.execute(text(sql), {"user_id":user_id})
    return result.fetchall()

def character_sheet(char_id):
    sql = "SELECT * FROM characters C WHERE C.id=:id"
    result = db.session.execute(text(sql), {"id":char_id})
    return result.fetchone()
