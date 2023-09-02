from flask import Flask 

app = Flask(__name__)
@app.route("/pagina um")
def oi():
    return "<b>EVANIR PFLEGER</b>"

@app. route("/paginadois")
def link():
    return "<a href=pagina um <clika aq></a>"


app.run(debug=True, host="0.0.0.0",port=4999)
