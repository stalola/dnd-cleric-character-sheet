from sqlalchemy.sql import text
from db import db
import users

def spellsheet(spell_id):
    sql = "SELECT * FROM spells S WHERE S.id=:id"
    result = db.session.execute(text(sql), {"id":spell_id})
    return result.fetchone()

def add_spell(name,level,cast_time, duration, range_area, components, school, attack_save, 
              damage_effect, description):
    user_id = users.user_id()
    if not users.is_user():
        return False
    sql = """INSERT INTO spells(name,level,cast_time,duration,range_area,components,school,
    attack_save,damage_effect,description)
    VALUES (:name,:level,:cast_time,:duration,:range_area,:components,:school,
    :attack_save,:damage_effect,:description)"""
    db.session.execute(text(sql), {"user_id":user_id, "name":name,"level":level,"cast_time":
                                   cast_time,"duration":duration,"range_area":range_area,
                                   "components":components,"school":school,"attack_save":
                                   attack_save,"damage_effect":damage_effect,"description":
                                   description})
    db.session.commit()
    return True
