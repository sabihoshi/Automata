import unittest

from ENFAFile import ENFA


class TestENFA(unittest.TestCase):

    def setUp(self) -> None:
        self.enfa = ENFA()

    # Test when the input_string is accepted
    def test_accepts_normal(self):
        self.enfa.start_state = 'q1'
        self.enfa.states = ['q1', 'q2']
        self.enfa.transitions = {('q1', 'ε'): ['q2'], ('q1', '1'): ['q1']}
        self.enfa.accept_states = ['q2']
        self.assertTrue(self.enfa.accepts(''))

    # Test when the input_string is accepted
    def test_accepts_true(self):
        self.enfa.start_state = 'q1'
        self.enfa.states = ['q1', 'q2']
        self.enfa.transitions = {('q1', 'ε'): ['q2'], ('q1', '1'): ['q1']}
        self.enfa.accept_states = ['q2']
        self.assertTrue(self.enfa.accepts('1'))

    # Test with no transitions defined
    def test_accepts_no_transitions(self):
        self.enfa.start_state = 'q1'
        self.enfa.states = ['q1', 'q2']
        self.enfa.transitions = {}
        self.enfa.accept_states = ['q2']
        self.assertFalse(self.enfa.accepts('1'))

    # Test epsilon closure
    def test_epsilon_closure(self):
        self.enfa.start_state = 'q1'
        self.enfa.states = ['q1', 'q2', 'q3']
        self.enfa.transitions = {('q1', 'ε'): ['q2'], ('q2', 'ε'): ['q3']}
        self.assertEqual(self.enfa.epsilon_closure(['q1']), {'q1', 'q2', 'q3'})

    # Test move function
    def test_move(self):
        self.enfa.start_state = 'q1'
        self.enfa.states = ['q1', 'q2']
        self.enfa.transitions = {('q1', '0'): ['q2']}
        self.assertEqual(self.enfa.move(['q1'], '0'), {'q2'})

    # Test when the input_string is accepted due to epsilon transition
    def test_accepts_epsilon_transition(self):
        self.enfa.start_state = 'q1'
        self.enfa.states = ['q1', 'q2']
        self.enfa.transitions = {('q1', 'ε'): ['q2']}
        self.enfa.accept_states = ['q2']
        self.assertTrue(self.enfa.accepts(''))
