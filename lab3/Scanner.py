import sys
sys.path.append('C:/Users/quackdratic/desktop/lftc/lftc-labs')

from lab2.SymbolTable import SymbolTable
from lab3.PIF import PIF

import re


class Scanner:
    def __init__(self):
        self.__ids = SymbolTable()
        self.__cts = SymbolTable()
        self.__pif = PIF()
        self.__split_regex = "(>=|<=|==|!=|\*\*|\*|>|<|%|\\+|-|=| |\(|\)|:|\{|\}|\[|\])"
        self.__identifier_regex = "^([a-zA-z]+)$"
        self.__int_regex = "^([+-]?[1-9][0-9]*)|(0)$"
        self.__string_regex = "^(\"[a-zA-z_-]*\")$"
        self.__reserved_regex = "^(i|s|if|el|run|in|out|\.|:|=|>|\\+|<|>=|<=|==|!=|\*\*|\*|\/|%|\(|\)|\{|\}|\[|\])$"
    
    def __scan_line(self, content, line_idx):
        tokens = re.split(self.__split_regex, content)
        if content[0] == '#':
            return
        for token in tokens:
            token = token.strip()
            if len(token) == 0:
                pass
            elif re.match(self.__reserved_regex, token) != None:
                self.__pif.add_reserved(token)
            elif re.match(self.__string_regex, token) or re.match(self.__int_regex, token):
                pos = self.__cts.add(token)
                self.__pif.add_constant(token)
            elif re.match(self.__identifier_regex, token):
                pos = self.__ids.add(token)
                self.__pif.add_identifier(pos)
            else:
                print("Error at line " + str(line_idx) + ": " + str(token))
                input()
    
    def scan_file(self, path):
        print(path)
        with open(path) as file:
            for idx, line in enumerate(file):
                self.__scan_line(line, idx)
        
        print(self.__ids)
        print(self.__cts)
        print(self.__pif)

