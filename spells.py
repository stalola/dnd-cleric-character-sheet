from sqlalchemy.sql import text
from db import db

def spellsheet(spell_id):
    sql = "SELECT * FROM spells S WHERE S.id=:id"
    result = db.session.execute(text(sql), {"id":spell_id})
    return result.fetchone()
