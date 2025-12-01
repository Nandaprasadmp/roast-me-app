from flask import Flask, render_template, request
import random

app = Flask(__name__)

roasts = [
    "Hey {name}, your code has more bugs than a rainy forest.",
    "{name}, even your laptop gets tired when you open your project.",
    "{name}, your debugging skills are as stable as your sleep schedule.",
    "Bro {name}, even ChatGPT gave up trying to fix your code.",
    "{name}, your WiFi runs faster than your brain on Mondays.",
    "{name}, your code works… only in your dreams.",
    "Relax {name}, even professional coders cry while debugging.",
    "{name}, your errors have their own errors.",
]

@app.route("/", methods=["GET", "POST"])
def home():
    roast_text = ""
    if request.method == "POST":
        username = request.form.get("username")
        if username:
            roast_text = random.choice(roasts).format(name=username)
    return render_template("index.html", roast=roast_text)

if __name__ == "__main__":
    app.run(debug=True)
