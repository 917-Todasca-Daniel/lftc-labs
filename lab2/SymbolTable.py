class SymbolTable:
    def __init__(self):
        self.__rolling_prime = 1123
        self.__buckets = [[] for _ in range(self.__rolling_prime)]
        self.__alphabet = [
            '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '"',
        ]

    def __hash_fn(self, x):
        str_x = str(x)
        i_hash = 0
        for char in str_x:
            i_hash = (i_hash * len(self.__alphabet) + self.__alphabet.index(char)) % self.__rolling_prime
        return i_hash

    def add(self, key):
        value = self.__hash_fn(key)

        if key not in self.__buckets[value]:
            self.__buckets[value].append(key)
        
        return value, self.__buckets[value].index(key)

        
