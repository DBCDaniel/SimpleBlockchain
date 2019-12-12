from block import Block

class Blockchain:
    """ The Blockchain class manages the chain of blocks as well as open
    transactions and the node on which it's running.

    Attributes:
        :chain: The list of blocks
        :open_transactions (private): The list of open transactions
    """
    def __init__(self, public_key, node_identifier):
        #starting block for the chain
        GENISIS_BLOCK = Block(0, "", [], 100, 0)
        #Initialize base blockchain list
        self.chain = [GENISIS_BLOCK]
        #Initalize base list of unhandled transactions
        self.__open_transactions = []
        #Assigning the public key
        self.public_key = public_key
        #Assigning the node identifier
        self.node_id = node_identifier
        #Load blockchain data
    
    #This turns the chain attribute into a property with a getter (the method
    #below) and a setter (@chain.setter)
    @property
    def chain(self):
        return self.__chain[:]
    #The setter for the chain prooperty
    @chain.setter
    def chain(self, val):
        self.__chain = val

    def get_balance(self):
        """ currently only a placeholder - returns 0 """
        return 0