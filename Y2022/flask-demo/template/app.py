from flask import Flask, render_template

app = Flask("__name__")
app.config.from_prefixed_env


@app.route("/watchlist")
def watch_list():
    return render_template("watchlist.html", user=user, movies=movies)
