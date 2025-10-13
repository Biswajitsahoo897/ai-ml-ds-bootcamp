from flask import Flask, render_template
app = Flask(__name__,static_url_path="/public")
@app.route("/")
def hello_world():
    return render_template("index.html")

app.run(debug=True);




# Notes
#app = Flask(__name__, static_folder='assets', static_url_path='/public')
# Flask finds static files inside the assets/ directory.
# Flask serves them from URLs like: http://localhost:5000/public/style.css
# (even though the actual file is located at assets/style.css)


# app = Flask(__name__,static_url_path="/public") 
# this is how u change the staic url path to public 
# ( can't access the style.css file inside the staic folder)