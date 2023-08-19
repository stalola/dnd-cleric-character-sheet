from flask import render_template, request, redirect
from app import app
import users
import characters
import spells


@app.route("/")
def index():
    chars = characters.get_characters()
    return render_template("index.html", chars=chars)


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        return redirect("/")
    return render_template("error.html", message="Wrong username or password")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords differ")
        if users.register(username, password1):
            return redirect("/")
        return render_template("error.html", message="Registration failed")


@app.route("/new_character", methods=["GET", "POST"])
def new_character():
    if request.method == "GET":
        allow = users.is_user()
        if not allow:
            return render_template("error.html", message="Not permitted")
        return render_template("new_character.html")
    if request.method == "POST":
        character_name = request.form["character_name"]
        speed = request.form["speed"]
        race = request.form["race"]
        level = request.form["level"]
        wisdom = request.form["wisdom"]
        strength = request.form["strength"]
        charisma = request.form["charisma"]
        dexterity = request.form["dexterity"]
        constitution = request.form["constitution"]
        intelligence = request.form["intelligence"]
        if characters.create(character_name, speed, race, level, wisdom, strength, charisma,
                             dexterity, constitution, intelligence):
            return redirect("/")
        return render_template("error.html", message="Creating new character failed")


@app.route("/character/<int:char_id>")
def character_page(char_id):
    character = characters.character_sheet(char_id)
    modifier = {"strength": characters.modifier(character.strength), "dexterity":
                characters.modifier(character.dexterity), "constitution":
                characters.modifier(character.constitution), "intelligence":
                characters.modifier(character.intelligence), "wisdom":
                characters.modifier(character.wisdom), "charisma":
                characters.modifier(character.charisma)}
    return render_template("character.html", character=character, modifier=modifier)


@app.route("/character/<int:char_id>/edit", methods=["GET", "POST"])
def character_edit(char_id):
    if request.method == "GET":
        allow = False
        character = characters.character_sheet(char_id)
        if users.user_id() == character.user_id:
            allow = True
        if not allow:
            return render_template("error.html", message="Not permitted")
        return render_template("edit_character.html", character=character)
    if request.method == "POST":
        char_id = request.form["character_id"]
        speed = request.form["speed"]
        level = request.form["level"]
        wisdom = request.form["wisdom"]
        strength = request.form["strength"]
        charisma = request.form["charisma"]
        dexterity = request.form["dexterity"]
        constitution = request.form["constitution"]
        intelligence = request.form["intelligence"]
        if characters.update(char_id, speed, level, wisdom, strength, charisma, dexterity,
                             constitution, intelligence):
            return redirect("/character/" + char_id)
        return render_template("error.html", message="Updating failed")


@app.route("/add_spell", methods=["GET", "POST"])
def new_spell():
    if request.method == "GET":
        allow = users.is_user()
        if not allow:
            return render_template("error.html", message="Not permitted")
        return render_template("add_spell.html")
    if request.method == "POST":
        name = request.form["name"]
        level = request.form["level"]
        cast_time = request.form["cast_time"]
        duration = request.form["duration"]
        range_area = request.form["range_area"]
        components = request.form["components"]
        school = request.form["school"]
        attack_save = request.form["attack_save"]
        damage_effect = request.form["damage_effect"]
        description = request.form["description"]
        if spells.add_spell(name, level, cast_time, duration, range_area, components, school,
                            attack_save, damage_effect, description):
            return redirect("/")
        return render_template("error.html", message="Adding new spell failed")


@app.route("/spell/<int:spell_id>", methods=["GET"])
def spell_page(spell_id):
    allow = users.is_user()
    if not allow:
        return render_template("error.html", message="Not permitted")
    spell = spells.spellsheet(spell_id)
    s_descr = spell.description
    s_descr = s_descr.split('\n')
    return render_template("spell.html", spell=spell, s_descr=s_descr)
