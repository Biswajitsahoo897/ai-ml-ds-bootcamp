from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    # name="Biswajit"
    # tokens=78230
    # Use .get() instead of direct indexing to avoid KeyError if query params are missing
    if 'name' in request.args:
        name = request.args.get('name', 'Guest')
    elif 'token' in request.args  :
        token = request.args.get('token', '0')
    else:
        name = 'Guest'
        token = '0'
    return render_template("index.html", name=name, token=token)

if __name__ == "__main__":
    app.run(debug=True)


#Query : http://127.0.0.1:5000/?name=jack&token=12312