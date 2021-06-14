from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
# a=False
 

@app.route("/")
def home():
    return render_template("index.html", content="testing")




# @app.route("/<name>")
# def user(nSame):
#     return f"hello {name}"

# @app.route("/admin/")
# def admin():
#     return redirect(url_for("user",name = "Admin"))

if __name__ == "__main__":
    app.run(debug=True)