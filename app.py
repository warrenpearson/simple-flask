from flask import Flask, render_template, request, make_response, jsonify


app = Flask(__name__)


@app.route("/")
@app.route("/one")
def do_one():
    return "Hello"


@app.route("/two")
def do_two():
    resp = make_response(render_template('index.html'))
    return resp


@app.route("/three")
def do_three():
    my_data = {"name": "warren"}

    resp = make_response(jsonify(my_data))
    return resp


@app.route("/four")
def do_four():
    name = request.args.get("name")

    if name is None:
        name = "Nobody"

    response = dict()
    response["supplied_name"] = name

    resp = make_response(jsonify(response))
    return resp


if __name__ == '__main__':
    app.run()
