from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO) 

@app.route("/")
def index():
    return jsonify(message="Welcome to Service 2", available_routes=["/ping", "/hello"])

@app.route("/ping")
def ping():
    return jsonify(status="ok", service="2")

@app.route("/hello")
def hello():
    return jsonify(message="Hello from Service 2")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
