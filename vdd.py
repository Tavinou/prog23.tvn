from flask import Flask 

app = Flask(__name__)
@app.route("/")
def oi():
    return "<b> blau blau </b>"
app.run(debug=True, host="0.0.0.0",port=4999)
