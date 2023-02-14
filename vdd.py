from flask import flask 

app = flask(__name__)
@app.route("/")
def oi():
    return "<b> oi </b>"
app.run()
