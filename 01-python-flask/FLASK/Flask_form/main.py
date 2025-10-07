from flask import Flask, render_template ,request

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def hello_world():
    print(request.method)
    if request.method == "POST":
        with open("File.txt",'w') as f:
            f.write(f"The name is :{request.form['name']} and Email address {request.form['email']}")
            f.close() 
            # This is just for the understanding purpose ,not recommended in the production level

            print(request.form)
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

