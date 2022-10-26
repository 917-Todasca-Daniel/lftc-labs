class PIF:
    def __init__(self):
        self.__tuples = []
    
    def add_reserved(self, val):
        self.__tuples.append((val, (-1, -1)))
    
    def add_constant(self, pos):
        self.__tuples.append(("const", pos))

    def add_identifier(self, pos):
        self.__tuples.append(("id", pos))
    
    def __str__(self):
        return str(self.__tuples) 
