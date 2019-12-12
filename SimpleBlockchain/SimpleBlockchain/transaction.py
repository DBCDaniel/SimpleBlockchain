from utility.printable import Printable
from collections import OrderedDict

class Transaction(Printable):
    """ A transaction which can be added to a block in the blockchain.

    Attributes:
        :sender: The sender of the transaction.
        :recipient: The recipient of the transaction.
        :signature: The signature of the transaction.
        :amount: the currency amount sent.
    """
    def __init__(self, sender, recipient, signature, amount):
        self.sender = sender
        self.recipient = recipient
        self.signature = signature
        self.amount = amount

    def to_ordered_dict():
        """ Converts this transaction into a OrderedDict."""
        return OrderedDict(
            [
                ("sender", self.sender),
                ("recipient", self.recipient),
                ("signature", self.signature),
                ("amount", self.amount)
            ]
        )