from Automaton import Automaton


class DFA(Automaton):
    def __init__(self):
        super().__init__()
        self.Title = "DETERMINISTIC FINITE AUTOMATA (DFA)"

    def input_dfa(self):
        print(self.doubleline + f"\n{self.Title.center(self.width)}\n" + self.singleline)
        print("You have selected: Deterministic Finite Automata! ")

        states_without_q = input("Enter the states (comma-separated): ").split(',')
        self.states = ['q' + states for states in states_without_q]
        self.alphabet = input("Enter the alphabet (comma-separated): ").split(',')
        print()

        print("Enter the next states for the following (enter . for dead/reject state)")
        for state in self.states:
            for alpha in self.alphabet:
                print(f"  \t  {alpha}")
                print(f"{state}\t---->\t", end="")

                while True:
                    dest_without_q = input()
                    dest_digits = ''.join(filter(str.isdigit, dest_without_q))

                    if not dest_without_q:
                        print("No input provided.\nPlease enter a valid state for this transition again: ", end="")
                        continue
                    elif dest_without_q == ".":
                        print("Invalid input.\nPlease enter a valid state for this transition again: ", end="")
                        continue
                    else:
                        dest_values = dest_without_q.split(',')
                        invalid_states = [dest for dest in dest_values if dest not in states_without_q]

                        if len(dest_values) > 1:
                            print("Invalid input: multiple states provided. Please enter a single state: ", end="")
                            continue
                        elif dest_digits not in states_without_q or invalid_states:
                            print(f"Invalid state(s): {', '.join(invalid_states)}")
                            print("Please enter valid state(s) for this transition again: ", end="")
                            continue
                        else:
                            dest = ['q' + item for item in dest_values[0]]
                            self.transitions[(state, alpha)] = dest
                            break

                # self.transitions[(state, alpha)] = dest

        print()
        self.start_state = input("Enter the start state: ")
        self.accept_states = input("Enter the accept states (please separate by space): ").split()

    def is_accepted(self, input_string: str) -> bool:
        current_state = self.start_state  # Initialize with the start state
        for char in input_string:
            current_state = self.transitions.get((current_state, char))
            if current_state is None:
                return False

        return current_state in self.accept_states

    def test_dfa(self):
        print(
            self.singleline + f"\n{self.Title.center(self.width)}\n{self.TestTitle.center(self.width)}\n" + self.singleline)
        input_string = input("Enter an input string: ")
        if self.is_accepted(input_string):
            print(f"\nThe DFA string '{input_string}' is ACCEPTED")
        else:
            print(f"\nThe DFA string '{input_string}' is REJECTED")
        print(self.doubleline)
        import main
        main.try_again(self)

    def dfa_print(self):
        self.input_dfa()
        self.print()
        self.test_dfa()
        print(self.doubleline)

        import main
        main.try_again(self)
