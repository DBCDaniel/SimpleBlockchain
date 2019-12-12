from flask import Flask, jsonify, request, send_from_directory;
from flask_cors import CORS
from blockchain import Blockchain
from wallet import Wallet

app = Flask(__name__)
CORS(app)

def function_not_implemented():
    response = {
        "message": "requested functionality is currently not implemented"
    }
    return jsonify(response), 501

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
    wallet.create_keys()
    if wallet.save_keys():
        global blockchain
        blockchain = Blockchain(wallet.public_key, port)
        response = {
            "public_key": wallet.public_key,
            "private_key": wallet.private_key,
            "funds": blockchain.get_balance()
        }
        
        return jsonify(response), 201
    else:
        response = {
            "message": "Saving Keys Failed."
        }
        return jsonify(response), 500

@app.route("/wallet", methods=["GET"])
def load_keys():
    return function_not_implemented()
#WALLET REQUESTS END


if __name__ == "__main__":
    port = 5000
    wallet = Wallet(port)
    blockchain = Blockchain(wallet.public_key, port)
    app.run(host="0.0.0.0", port=port)