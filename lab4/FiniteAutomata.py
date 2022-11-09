from collections import defaultdict


class FiniteAutomata:
    def __init__(self):
        self.__alphabet = set()
        self.__states = defaultdict(list)

    def add_state(self, state):
        self.__states[state.get_token()] = state

    def get_state(self, token):
        if token not in self.__states.keys():
            raise Exception("Additing transition wth invalid state!")
        return self.__states[token]
    
    def get_states(self):
        return self.__states.values()

    def get_alphabet(self):
        return self.__alphabet

    def add_to_aphabet(self, char):
        self.__alphabet.add(char)

    def add_transition(self, src, where, how):
        if how not in self.__alphabet:
            raise Exception("Additing transition wth invalid alphabet!")
        src_state = self.get_state(src)
        dest_state = self.get_state(where)
        src_state.add_transition(dest_state, how)
    
    def is_DFA(self):
        for state in self.__states.values():
            if not state.is_DFA():
                return False
        return True
    
    def accept(self, word):
        now = None
        for state in self.__states.values():
            if state.is_initial():
                now = state
                break

        idx = 0
        while idx < len(word):
            edges = now.get_transitions()
            if word[idx] in edges.keys():
                now = edges[word[idx]][0]
                idx += 1 
            else:
                return False
        return idx == len(word) and now.is_final()
