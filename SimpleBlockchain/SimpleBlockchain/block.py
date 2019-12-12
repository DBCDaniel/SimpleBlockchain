from utility.printable import Printable
from time import time

class Block(Printable):
    """A single block of the blockchain.

    Attributes:
        :index: The index of this block.
        :prev_hash: The hash of the previous block in the blockchain.
        :transactions: A list of transactions which is contained in the block.
        :proof: The proof of work number that yielded this block.
        :timestamp: the timestamp of the block (default: automatically generated)
    """
    def __init__(self, index, prev_hash, transactions, proof, timestamp = None):
        self.index = index
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.proof = proof
        self.timestamp = time() if timestamp is None else timestamp