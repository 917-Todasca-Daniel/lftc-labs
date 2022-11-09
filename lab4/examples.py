from FAFactory import FAFactory


# FA = FAFactory.read_FA("C:\\Users\\quackdratic\\Desktop\\lftc\\lftc-labs\\lab4\\NDFA.in")
# FA = FAFactory.read_FA("C:\\Users\\quackdratic\\Desktop\\lftc\\lftc-labs\\lab4\\FA.in")
# FA = FAFactory.read_FA("C:\\Users\\quackdratic\\Desktop\\lftc\\lftc-labs\\lab4\\largeFA.in")
FA = FAFactory.read_FA("C:\\Users\\quackdratic\\Desktop\\lftc\\lftc-labs\\lab4\\FA_int.in")
# FA = FAFactory.read_FA("C:\\Users\\quackdratic\\Desktop\\lftc\\lftc-labs\\lab4\\FA_err.in")


can_accept = True
if FA.is_DFA():
    print("Is DFA!")
else:
    print("Is not DFA.")
    can_accept = False

option = -1
while option != 0:
    print("1 - states, 2 - alphabet, 3 - transitions, 4 - initial, 5 - final, 6 - accept")
    option = int(input())
    if option == 1:
        for state in FA.get_states():
            print(state)
    elif option == 2:
        print(FA.get_alphabet())
    elif option == 3:
        for state in FA.get_states():
            for how, where in state.get_transitions().items():
                for other in where:
                    print("{0} -> {2} ({1})".format(state.get_token(), how, other.get_token()))
    elif option == 4:
        for state in FA.get_states():
            if state.is_initial():
                print(state)
    elif option == 5:
        for state in FA.get_states():
            if state.is_final():
                print(state)
    elif option == 6:
        if not can_accept:
            continue
        while True:
            str = input()
            print(FA.accept(str))
