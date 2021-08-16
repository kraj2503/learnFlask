from flask import Flask, redirect, url_for, render_template, request, session, flash
from  datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# a=False
app.secret_key="hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.permanent_session_lifetime= timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id=db.column("Id",db.Integer, primary_key=True)
    name= db.column("name",db.string(100))
    email=db.column("email",db.string(100))
    

    def __init__(self,name,email):
        self.name=name
        self.email=email

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods= ["POST" ,"GET"])
def login():
    if request.method == "POST":
      session.permanent = True
      user = request.form["nm"]
      session["user"]=user
      flash("login succesfull")
      return redirect(url_for("user"))
    else:
        if "user" in  session:
            flash("Ald loged in!")
            return redirect(url_for("user"))
        return render_template("login.html")



@app.route("/user", methods={"POST","GET"})
def user():
    email=None
    if "user" in session:
        user = session["user"]
        if request.method=="POST":
            email=request.form["email"]
            session["email"]= email
            flash("email was saved")
        else:
            if "email" in session:
                email=session["email"] 
        return render_template("user.html",email=email)
    else:
        flash("you are ald logged in!")
        return redirect(url_for("login"))




@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        session.pop("user",None)
        session.pop("email",None)
        flash("you have been log out!", "info")
    return redirect(url_for("login"))

# @app.route("/<name>")
# def user(nSame):
#     return f"hello {name}"

# @app.route("/admin/")
# def admin():
#     return redirect(url_for("user",name = "Admin"))

if __name__ == "__main__":
    db.create_all
    app.run(debug=True)