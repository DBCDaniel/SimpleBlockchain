class Printable:
    """ A base class which implements prinitng functionality """
    def __repr__(self):
        return str(self.__dict__)
