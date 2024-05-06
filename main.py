from flask import Flask
from flask import render_template
from flask import jsonify, request

webapp=Flask(__name__)

@webapp.route("/")
def minimal_f():
    return "<p>This is Minimal Application in Flask!</p>"

@webapp.route("/routing")
def routing():
    return "<p>This is routing!</p>"

@webapp.route("/templates")
def templates():
    return render_template("index.html")



@webapp.route("/API/flavours/<flavour_name>")
def ice_cream_GET(flavour_name):
    result={
        "Flavour": f'{flavour_name}'
    }
    return jsonify(result)


webapp.run(debug=True)
