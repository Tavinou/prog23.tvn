from flask import Flask 

app = Flask(__name__)
@app.route("/")
def oi():
    return "<b> baleia 2 </b>"
app.run(port=4999)
