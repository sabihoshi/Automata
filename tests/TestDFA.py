import unittest

from DFAFile import DFA


class TestDFA(unittest.TestCase):

    def setUp(self) -> None:
        self.dfa = DFA()

    # Test when the input_string is accepted
    def test_is_accepted_normal(self):
        self.dfa.start_state = 'q1'
        self.dfa.transitions = {('q1', '0'): 'q2', ('q1', '1'): 'q1'}
        self.dfa.accept_states = ['q2']
        self.assertTrue(self.dfa.is_accepted('0'))

    # Test when the input_string is not accepted
    def test_is_accepted_fail(self):
        self.assertFalse(self.dfa.is_accepted('1'))

    # Test with no transitions defined
    def test_is_accepted_no_transitions(self):
        self.dfa.transitions = {}
        self.assertFalse(self.dfa.is_accepted('0'))

    def test_is_rejected_empty_string(self):
        self.dfa.start_state = 'q1'
        self.dfa.transitions = {('q1', '0'): 'q2', ('q1', '1'): 'q1'}
        self.dfa.accept_states = ['q2']
        self.assertFalse(self.dfa.is_accepted(''))

    def test_is_rejected_long_string(self):
        self.dfa.start_state = 'q1'
        self.dfa.transitions = {('q1', '0'): 'q2', ('q1', '1'): 'q1'}
        self.dfa.accept_states = ['q2']
        self.assertFalse(self.dfa.is_accepted('000000'))  # Modify accordingly

    def test_is_accepted_no_accept_state(self):
        self.dfa.start_state = 'q1'
        self.dfa.transitions = {('q1', '0'): 'q2', ('q1', '1'): 'q1'}
        self.dfa.accept_states = []
        self.assertFalse(self.dfa.is_accepted('0'))

    def test_is_accepted_multiple_accept_states(self):
        self.dfa.start_state = 'q1'
        self.dfa.transitions = {('q1', '0'): 'q2', ('q1', '1'): 'q1', ('q2', '0'): 'q3'}
        self.dfa.accept_states = ['q2', 'q3']
        self.assertTrue(self.dfa.is_accepted('00'))