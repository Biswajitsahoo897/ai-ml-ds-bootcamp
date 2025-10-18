from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():

    marks={
        "Biswajit":67,
        "Jigzs":99,
        "saswat":40,
        "riya":30,
        "Sohum":100
    }
    
    values=[1,marks,67]
    return jsonify(values)
    # return jsonify(marks)


app.run(debug=True)