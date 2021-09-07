from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "http://6b0b-35-185-107-52.ngrok.io/"

@app.route("/")
def index():
    req = requests.get(url)
    JSON = req.json()
    return render_template("index.html", lista=JSON)


if __name__ == '__main__':
    app.run()
