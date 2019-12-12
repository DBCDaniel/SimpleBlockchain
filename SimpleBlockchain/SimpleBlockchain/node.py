from flask import Flask, jsonify, request, send_from_directory;
from flask_cors import CORS
from blockchain import Blockchain

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def get_node_ui():
    return send_from_directory("ui", "node.html")

if __name__ == "__main__":
    blockchain = Blockchain()
    app.run(host="0.0.0.0", port=5000)