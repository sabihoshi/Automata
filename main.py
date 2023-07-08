import NFAFile
import DFAFile
import ENFAFile
import Convert
import Automaton

#Titles
WelcomeTitle = "Welcome to our Mini Finite Automata Program!"
width = 70
singleline = "-" * width
doubleline = "=" * width

def main():
    print(doubleline + f"\n{WelcomeTitle.center(width)}\n" + singleline)
    print(f"{'':<18}What process would you like to do?")
    print(f"{'':<18}1. NFA")
    print(f"{'':<18}2. DFA")
    print(f"{'':<18}3. eNFA")
    print(f"{'':<18}4. eNFA -> NFA -> DFA")
    print(singleline)
    automaton_type = input("Please enter the corresponding number of selected automaton type:")
    print()

    if automaton_type == "1":
        automaton = NFAFile.NFA()
        automaton.nfa_print()
    elif automaton_type == "2":
        automaton = DFAFile.DFA()
        automaton.dfa_print()
    elif automaton_type == "3":
        automaton = ENFAFile.ENFA()
        automaton.enfa_print()
    elif automaton_type == "4":
        automaton = Convert.Convert()
        automaton.nfa2dfa_print()
    else:
        print("Invalid automaton type. Please enter the number of the option")
        return


def try_again(automaton: Automaton):
    print("Do you want to try again?")
    print("1. Test another string")
    print("2. Go back to Main Menu")
    print("3. Exit the program")
    print()
    choice = input("Enter your choice: ")

    if choice == "1":
        if isinstance(automaton, NFAFile.NFA):
            automaton.test_nfa()
        elif isinstance(automaton, DFAFile.DFA):
            automaton.test_dfa()
        elif isinstance(automaton, ENFAFile.ENFA):
            automaton.test_enfa()
        else:
            print("Invalid automaton type. Please enter the number of the option")
            return
    elif choice == "2":
        import main
        main.main()
    elif choice == "3":
        print()
        print("Thank you for using our program!")
        exit()
    else:
        print("invalid input")
        try_again(automaton)


if __name__ == "__main__":
    main()