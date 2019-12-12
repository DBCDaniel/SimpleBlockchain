class Blockchain:
    """ The Blockchain class manages the chain of blocks as well as open
    transactions and the node on which it's running.

    Attributes:
        :chain: The list of blocks
        :open_transactions (private): The list of open transactions
    """
    def __init__(self):
        #starting block for the chain
        GENISIS_BLOCK = {}
        #Initialize base blockchain list
        self.chain = [GENISIS_BLOCK]
        #Initalize base list of unhandled transactions
        self.__open_transactions = []
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