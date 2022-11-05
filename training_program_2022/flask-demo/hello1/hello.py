from flask import Flask, request, redirect, url_for, make_response, json, jsonify

app = Flask(__name__)


@app.route("/hello")
def hello_man():
    name = request.args.get("name", "Flask")
    return "<h1> hello, %s </h1>" % name


@app.route("/goback/<int:year>")
def go_back(year):
    return "<p> welcome to %d! </p>" % (2018 - year)


@app.route("/hi")
def hi():
    return redirect(url_for("hello_man"))


@app.route("/foo")
def foo():
    data = {"name": "Jeffrey", "gender": "male"}
    response = make_response(json.dumps(data))
    response.mimetype = "application/json"
    return response


@app.route("/foojson")
def foo_json():
    return jsonify({"name": "Jeffrey", "gender": "male"})
