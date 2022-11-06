from flask import (
    Flask,
    request,
    redirect,
    url_for,
    make_response,
    json,
    jsonify,
    session,
    abort,
)

app = Flask(__name__)
app.config.from_prefixed_env()


@app.route("/")
def index():
    return redirect(url_for("login_user"))


@app.route("/login")
def login_user():
    session["logged_in"] = True
    return redirect(url_for("hello_man"))


@app.route("/hello")
def hello_man():
    name = request.args.get("name", "Flask")
    if name is None:
        name = request.cookies.get("name", "alex")
    response_str = "<h1> hello, %s </h1>" % name

    if "logged_in" in session:
        response_str += "[Authenticated]"
    else:
        response_str += "[Not Authenticated]"

    return response_str


@app.route("/goback/<int:year>")
def go_back(year):
    return "<p> welcome to %d! </p>" % (2018 - year)


@app.route("/hi")
def hi_man():
    return redirect(url_for("hello_man"))


@app.route("/foo")
def foo_json():
    data = {"name": "Jeffrey", "gender": "male"}
    response = make_response(json.dumps(data))
    response.mimetype = "application/json"
    return response


@app.route("/foojson")
def foo_jsonify():
    return jsonify({"name": "Jeffrey", "gender": "male"})


@app.route("/set/<name>")
def set_cookie(name):
    response = make_response(redirect(url_for("hello_man")))
    response.set_cookie("name", name)
    return response


@app.route("/admin")
def admin_mgt():
    if "logged_in" not in session:
        abort(403)

    return "welcome to admin page"


@app.route("/logout")
def logout_user():
    if "logged_in" in session:
        session.pop("logged_in")
    return redirect(url_for("hello_man"))
