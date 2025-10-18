from flask import Flask,render_template,flash

app = Flask(__name__)

app.secret_key="23r9jfwgfbjfbyugwery9bwfu8uerjn"

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out!","success")
    return render_template("logout.html")

if __name__ == "__main__":
    app.run(debug=True)