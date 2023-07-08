from Automaton import Automaton


class ENFA(Automaton):
    def __init__(self):
        super().__init__()
        self.Title = "NON-DETERMINISTIC FINITE AUTOMATA WITH EPSILON TRANSITION (ε-NFA)"

    def input_enfa(self):
        print(self.doubleline + f"\n{self.Title.center(self.width)}\n" + self.singleline)
        print("You have selected: Epsilon Non-Deterministic Finite Automata! ")

        states_without_q = input("Enter the states (comma-separated): ").split(',')
        self.states = ['q' + states for states in states_without_q]

        self.alphabet = input("Enter the alphabet (comma-separated): ").split(',')
        self.alphabet.append("ε")
        print(self.states)

        print("Enter the next states for the following (enter . for dead/reject state)")
        for state in self.states:
            for alpha in self.alphabet:
                print(f"  \t  {alpha}")
                print(f"{state}\t---->\t", end="")

                while True:
                    dest_without_q = input()

                    if dest_without_q == "." or not dest_without_q:
                        self.transitions[(state, alpha)] = set()
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

        print()
        self.start_state = input("Enter the start state: ")
        self.accept_states = input("Enter the accept states (comma-separated): ").split(',')


    def epsilon_closure(self, states):
        closure = set(states)

        # while the closure is still being increased
        while True:
            new_states = set(s for state in closure
                             if (state, 'ε') in self.transitions
                             for s in self.transitions[(state, 'ε')]) - closure

            if not new_states:
                return closure

            closure |= new_states

    def move(self, states, symbol):
        moves = set()
        for state in states:
            if (state, symbol) in self.transitions:
                moves |= set(self.transitions[(state, symbol)])
        return moves

    def accepts(self, input_string):
        current_states = self.epsilon_closure([self.start_state])

        for symbol in input_string:
            current_states = self.epsilon_closure(self.move(current_states, symbol))

        return any(state in self.accept_states for state in current_states)

    def test_enfa(self):
        print(
            self.singleline + f"\n{self.Title.center(self.width)}\n{self.TestTitle.center(self.width)}\n" + self.singleline)
        input_string = input("Enter an input string: ")
        if self.accepts(input_string):
            print(f"\nThe ε-NFA string '{input_string}' is ACCEPTED")
        else:
            print(f"\nThe ε-NFA string '{input_string}' is REJECTED")
        print(self.doubleline)
        import main
        main.try_again(self)

    def enfa_print(self):
        self.input_enfa()
        self.print()
        self.test_enfa()
        print(self.doubleline)

        import main
        main.try_again(self)
