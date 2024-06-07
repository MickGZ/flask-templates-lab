from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("postal.html")

@app.route("/email", methods=["GET", "POST"])
def email():
    if request.method == "POST":
        postal_code = request.form["postal"]
        print(f"EMAIL PAGE - Value of postal: {postal_code}")
    return render_template("email.html")

@app.route("/name", methods=["GET", "POST"])
def name_view():
    if request.method == "POST":
        email = request.form["email"]
        print(f"NAME PAGE - Value of email: {email}")
    return render_template("name.html")

@app.route("/phone", methods=["GET", "POST"])
def phone():
    if request.method == "POST":
        name = request.form["name"]
        print(f"PHONE PAGE - value of name: {name}")
    return render_template("phone.html")

@app.route("/birthday", methods=["GET", "POST"])
def birthday():
    if request.method == "POST":
        phone = request.form["phone"]
        print(f"BIRTHDAY PAGE - value of phone: {phone}")
    return render_template("birthday.html")

@app.route("/offer", methods=["GET", "POST"])
def offer():
    if request.method == "POST":
        year = request.form["year"]
        month = request.form["month"]
        day = request.form["day"]
        print(f"OFFER PAGE - Year: {year}, Month: {month}, Day: {day}")
    return render_template("offer.html")
