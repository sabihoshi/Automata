from Automaton import Automaton


class NFA(Automaton):
    def __init__(self):
        super().__init__()
        self.Title = "NONDETERMINISTIC FINITE AUTOMATA (NFA)"



    def input_nfa(self):
        print(self.doubleline + f"\n{self.Title.center(self.width)}\n" + self.singleline)
        print("You have selected: Non-Deterministic Finite Automata! ")

        states_without_q = input("Enter the states (comma-separated): ").split(',')
        self.states = ['q' + state for state in states_without_q]
        print(self.states)

        self.alphabet = input("Enter the alphabet (comma-separated): ").split(',')
        print(self.alphabet)

        print("Enter the next states for the following (enter . for dead/reject state)")
        for state in self.states:
            for alpha in self.alphabet:
                print(f"  \t  {alpha}")
                print(f"{state}\t---->\t", end="")

                while True:
                    dest_without_q = input()

                    if dest_without_q == "." or not dest_without_q:
                        self.transitions[(state, alpha)] = "ø"
                        break
                    else:
                        dest_values = dest_without_q.split(',')
                        invalid_states = [dest for dest in dest_values if dest not in states_without_q]

                        if invalid_states:
                            print(f"Invalid state(s): {', '.join(invalid_states)}")
                            print("Please enter valid state(s) for this transition again: ", end="")
                        else:
                            dest = ['q' + item for item in dest_values]
                            self.transitions[(state, alpha)] = dest
                            break

        print(self.transitions)

        self.start_state = input("Enter the start state: ")
        self.accept_states = input("Enter the accept states (comma-separated): ").split(',')

    def is_accepted(self, input_string: str) -> bool:
        current_states = {self.start_state}
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if (state, symbol) in self.transitions:
                    next_states.update(self.transitions[(state, symbol)])
            current_states = next_states
        return bool(current_states.intersection(self.accept_states))


    def test_nfa(self):
        print(self.singleline + f"\n{self.Title.center(self.width)}\n{self.TestTitle.center(self.width)}\n" + self.singleline)
        input_string = input("Enter an input string: ")
        if self.is_accepted(input_string):
            print(f"\nThe NFA string '{input_string}' is ACCEPTED")
        else:
            print(f"\nThe NFA string '{input_string}' is REJECTED")
        print(self.doubleline)
        import main
        main.try_again(self)

    def nfa_print(self):
        self.input_nfa()
        self.print()
        self.test_nfa()
        print(self.doubleline)

        import main
        main.try_again(self)