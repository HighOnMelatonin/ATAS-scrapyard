from flask import Flask, render_template, redirect, url_for, request

app=Flask(__name__)

@app.route("/") #default page
def home():
    return render_template("index.html") #display index.html in templates folder

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":                      #if user submits data to nm
        user=request.form["material"]               #stores material variable into user
        return redirect(url_for("user",usr=user))   #redirects into user route
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{"You entered {}. Have a nice day!".format(usr)}</h1>"

if __name__=="__main__":
    app.run()