import sys
sys.path.append('C:/Users/quackdratic/desktop/lftc/lftc-labs')

from lab2.SymbolTable import SymbolTable
from lab3.PIF import PIF

import re
from pprint import pprint


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
            return False
        prev_type = None
        has_error = False
        for token_idx, token in enumerate(tokens):       
            token = token.strip()
            if token in ["+", "-"] and prev_type not in ["ct", "id"] and token_idx + 1 < len(tokens):
                tokens[token_idx+1] = token + tokens[token_idx+1]
                continue
            if len(token) == 0:
                pass
            elif re.match(self.__reserved_regex, token) != None:
                self.__pif.add_reserved(token)
                prev_type = "reserved"
            elif re.match(self.__string_regex, token) or re.match(self.__int_regex, token):
                pos = self.__cts.add(token)
                self.__pif.add_constant(token)
                prev_type = "ct"
            elif re.match(self.__identifier_regex, token):
                pos = self.__ids.add(token)
                self.__pif.add_identifier(pos)
                prev_type = "ct"
            else:
                has_error = True
                print("Error at line " + str(line_idx) + ": " + str(token))
                input()
        return has_error
    
    def scan_file(self, path):
        print(path)
        has_error = False
        with open(path) as file:
            for idx, line in enumerate(file):
                has_error |= self.__scan_line(line, idx)
        if has_error:
            print("Lexically correct!")
        
        with open('PIF.out', 'w') as file:
            pprint(str(self.__pif), stream=file)
        with open('ST.out', 'w') as file:
            print("Identifiers:", file=file)
            pprint(str(self.__ids), stream=file)
            print("Constants:", file=file)
            pprint(str(self.__cts), stream=file)

        print(self.__ids)
        print(self.__cts)
        print(self.__pif)

