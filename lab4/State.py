from collections import defaultdict


class State:
    def __init__(self, token, initial=False, final=False):
        self.__transitions = defaultdict(list)
        self.__token = token
        self.__final = final
        self.__initial = initial

    def set_final(self, value):
        self.__final = value

    def is_final(self):
        return self.__final

    def set_initial(self, value):
        self.__initial = value

    def is_initial(self):
        return self.__initial

    def get_token(self):
        return self.__token

    def add_transition(self, state, char):
        self.__transitions[char].append(state)
    
    def get_transitions(self):
        return self.__transitions
    
    def is_DFA(self):
        for _, value in self.__transitions.items():
            if len(value) > 1:
                return False
        return True

    def __str__(self):
        return "Token: " + self.__token + \
            ", Initial: " + str(self.__initial) + \
            ", Final: " + str(self.__final)
