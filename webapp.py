from flask import Flask, render_template, request
from main import get_followers, get_locations, processing_locations, create_map

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/enter_screen_name", methods=["POST"])
def submit():
    if not request.form.get("screen_name") or not request.form.get("bearer_token"):
        if not request.form.get("counter"):
            return render_template("failure.html")
    screen_name = request.form.get("screen_name")
    token = request.form.get("bearer_token")
    counter = request.form.get("counter")
    followers = get_followers(screen_name, token, counter)
    locations = get_locations(followers)
    new_locations = processing_locations(locations)
    create_map(new_locations)
    return render_template("some.html")
