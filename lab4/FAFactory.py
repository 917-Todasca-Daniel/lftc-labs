from State import State
from FiniteAutomata import FiniteAutomata


class FAFactory:
    def read_FA(file_path):

        FA = FiniteAutomata()
        with open(file_path) as file:
            alphabet_line = file.readline()
            for char in alphabet_line.split(","):
                char = char.strip()
                assert len(char) <= 1
                FA.add_to_aphabet(char)

            state_line = file.readline()
            for token in state_line.split(","):
                token = token.strip()
                FA.add_state(State(token))

            initial_line = file.readline()
            initial_line = initial_line.strip()
            FA.get_state(initial_line).set_initial(True)

            final_line = file.readline()
            for token in final_line.split(","):
                token = token.strip()
                FA.get_state(token).set_final(True)

            transition_line = file.readline()
            while transition_line:
                src, how, where = transition_line.split(",")
                where = where.strip()
                assert how in FA.get_alphabet()
                FA.add_transition(src, where, how)
                transition_line = file.readline()

        return FA