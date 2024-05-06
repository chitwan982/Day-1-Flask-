from flask import Flask

webapp=Flask(__name__)

@webapp.route("/")
def minimal_f():
    return "<p>This is Minimal Application in Flask!</p>"

webapp.run(debug=True)
