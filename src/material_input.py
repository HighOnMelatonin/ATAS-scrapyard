from flask import Flask, render_template, redirect, url_for, request

app=Flask(__name__)

@app.route("/") #default page
def home():
    if request.method=="POST":
        user=request.form("user")
        return redirect(url_for("material",user))
    else:
        return render_template("index.html") #display index.html in templates folder

@app.route("/material",methods=["POST","GET"])
def material():
    if request.method=="POST":                      #if user submits data to nm
        user=request.form["material"]               #stores material variable into user
        return redirect(url_for("user",usr=user))   #redirects into user route
    else:
        return render_template("material.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{'You entered {}. Have a nice day!'.format(usr)}</h1>"

if __name__=="__main__":
    app.run(debug=True)