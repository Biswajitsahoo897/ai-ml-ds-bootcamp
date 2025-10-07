from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        "alex":34,
        "Joe":80,
        "Lily":60,
        "Raj":92,
        "Max":12,
        "Jesse":100,
        "Robert":90
    }
    # Jinja2  basic template    
    return render_template("index.html",marks=marks)

if __name__ == "__main__":
    app.run(debug=True)
