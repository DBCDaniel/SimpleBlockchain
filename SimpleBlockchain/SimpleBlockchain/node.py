from flask import Flask, jsonify, request, send_from_directory;
from flask_cors import CORS
from blockchain import Blockchain

app = Flask(__name__)
CORS(app)

#WEB INTERFACE START
@app.route("/", methods=["GET"])
def get_node_ui():
    return send_from_directory("ui", "node.html")

@app.route("/network", methods=["GET"])
def get_network_ui():
    return send_from_directory("ui", "network.html")
#WEB INTERFACE END

#WALLET REQUESTS START
@app.route("/wallet", methods=["POST"])
def create_keys():
    response = {
        "message": "requested functionality is currently not implemented"
    }
    return jsonify(response), 501


@app.route("/wallet", methods=["GET"])
def load_keys():
    response = {
        "message": "requested functionality is currently not implemented"
    }
    return jsonify(response), 501
#WALLET REQUESTS END


if __name__ == "__main__":
    blockchain = Blockchain()
    app.run(host="0.0.0.0", port=5000)