from FLASK import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
    # return "<p>Hello, World!</p>"

app.run(debug=True) # u can do this to run the flask app 
# just type flask --app main(which is the file name) run