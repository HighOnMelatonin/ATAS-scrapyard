from flask import Flask, render_template, redirect, url_for, request
import manager
import json

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def home():
    ## Format the market dictionary to display to the user
    file = open("test_market.json", "r+")
    market = json.load(file)
    file.close()
    
    return render_template('index.html', market=market)

@app.route("/material", methods=["POST", "GET"])
def material():
    if request.method == "POST":
        user = request.form.get("user")
        material = request.form.get("material")

        ## Format the market dictionary to display to the user
        file = open("test_market.json", "r+")
        market = json.load(file)
        file.close()

        ## Check if user exists, if not, create new user
        users = manager.openJson()
        users = manager.createUser(user, users)

        points = manager.getPoints(material)
        donating = request.form.get("donating")
        manager.changeQty(material, market, donating)

        if donating == "on":
            manager.changePoints(points, user, users)

        else:
            manager.changePoints(-points, user, users)

        manager.commitJson(users, "test_user.json")
        manager.commitJson(market, "test_market.json")

        return redirect(url_for("user", user=user))

    else:
        return render_template('material.html', user = user)

@app.route('/<user>')
def user(user):
    ## Format the market dictionary to display to the user
    file = open("test_market.json", "r+")
    market = json.load(file)
    file.close()

    users = manager.openJson()
    points = users[user]
    print(user, points)

    return render_template('goodbye.html', user=user, points=points, market=market)

if __name__ == "__main__":
    app.run(debug=True)


