from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import Crypto.Random as rnd
import binascii

class Wallet:
    """Creates, load and holdes private and public keys, 
    used to manage transaction signing and verification.
    """
    def __init__(self, node_identifier):
        self.private_key = None
        self.public_key = None
        self.node_identifier = node_identifier

    def generate_keys(self):
        """ Generates a new pair of private and public key."""
        private_key = RSA.generate(1024, rnd.new().read)
        public_key = private_key.publickey()
        return (
            binascii.hexlify(private_key.export_key(format="DER"))
            .decode("ascii"),
            binascii.hexlify(public_key.export_key(format="DER"))
            .decode("ascii")
        )

    def create_keys(self):
        """Creates a new pair of private and public keys."""
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key

    def save_keys(self):
        """ Saves the keys to a file (savefiles/wallet.dat) """
        if self.public_key is not None and self.private_key is not None:
            filePath = "savefiles/wallet[{0}].dat".format(self.node_identifier)
            try:
                with open(filePath, mode="w") as writer:
                    writer.write(self.public_key)
                    writer.write("\n")
                    writer.write(self.private_key)
                return True
            except(IOError, IndexError):
                print("Wallet Saving Failed...")
                return False