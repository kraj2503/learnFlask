from flask import Flask, redirect, url_for, render_template, request, session, flash
from  datetime import timedelta
app = Flask(__name__)
# a=False
app.secret_key="hello"
app.permanent_session_lifetime= timedelta(minutes=5)


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

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html",user = user)
    else:
        flash("you are ald logged in!")
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        session.pop("user",None)
        flash("you have been log out!", "info")
    return redirect(url_for("login"))

# @app.route("/<name>")
# def user(nSame):
#     return f"hello {name}"

# @app.route("/admin/")
# def admin():
#     return redirect(url_for("user",name = "Admin"))

if __name__ == "__main__":
    app.run(debug=True)