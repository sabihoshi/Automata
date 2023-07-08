from Automaton import Automaton
from NFAFile import NFA
from DFAFile import DFA

class Convert(Automaton):
    def __init__(self):
        super().__init__()

    class ConvertNFA2DFA():

        def convert_nfa_to_dfa(self, nfa: NFA) -> DFA:
            dfa = DFA()
            dfa.states = nfa.states  # DFA states are the same as NFA states initially
            dfa.alphabet = nfa.alphabet
            dfa.start_state = nfa.start_state
            dfa.accept_states = nfa.accept_states

            unmarked_states = [dfa.start_state]  # Unmarked states in the DFA
            marked_states = []  # Marked states in the DFA

            while unmarked_states:
                current_state = unmarked_states.pop()
                marked_states.append(current_state)

                for symbol in dfa.alphabet:
                    next_states = set()
                    for nfa_state in current_state:
                        if (nfa_state, symbol) in nfa.transitions:
                            next_states.update(nfa.transitions[(nfa_state, symbol)])

                    if next_states:
                        dfa.transitions[(current_state, symbol)] = next_states

                        if next_states not in marked_states and next_states not in unmarked_states:
                            unmarked_states.append(next_states)

            return dfa

        def nfa2dfa_print(self):
            nfa = NFA()
            nfa.input_nfa()
            nfa.print()

            dfa = self.convert_nfa_to_dfa(nfa)
            dfa.print()
            dfa.test_dfa()

            print(self.doubleline)

            import main
            main.try_again(self)
