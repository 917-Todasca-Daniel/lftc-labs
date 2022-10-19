from SymbolTable import SymbolTable

ids = SymbolTable()
cts = SymbolTable()

identifiers = [
    "a", "a", "b", "c", "d", "e", "f", "g", "aAbBcC",
    "Max", "Min", "message", "intValue", "stringOutput",
    "_Max", "_Min", "_message", "_intValue", "_stringOutput",
]

constants = [
    "0", "1", "2", "3", "4", "5", "6", '"0"', '"1"', '"2"', '"3"', '"4"', '"5"', '"6"',
    "string-constant", "another_string", "Task-run-successfully_",
]

for val in identifiers:
    print(val, ids.add(val), ids.add(val))

for val in constants:
    print(val, cts.add(val), cts.add(val))