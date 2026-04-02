from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Name: Durva Chhabria</h2>
    <h3>AppID: 2404713</h3>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
