import unittest

from NFAFile import NFA


class TestNFA(unittest.TestCase):

    def setUp(self) -> None:
        self.nfa = NFA()

    # Test when input_string leads to an accepted state
    def test_is_accepted_normal(self):
        self.nfa.start_state = 'q1'
        self.nfa.transitions = {('q1', '0'): ['q2'], ('q1', '1'): ['q1']}
        self.nfa.accept_states = ['q2']
        self.assertTrue(self.nfa.is_accepted('0'))

    def test_is_accepted_multiple_transitions(self):
        self.nfa.start_state = 'q1'
        self.nfa.transitions = {('q1', '0'): ['q2', 'q3'], ('q1', '1'): ['q1']}
        self.nfa.accept_states = ['q2']
        self.assertTrue(self.nfa.is_accepted('0'))

    # Test when input_string does not lead to an accepted state
    def test_is_accepted_fail(self):
        self.assertFalse(self.nfa.is_accepted('1'))

    # Test when input_string is an empty string
    def test_is_accepted_empty(self):
        self.assertFalse(self.nfa.is_accepted(''))  # Assuming empty string is not accepted

    def test_is_accepted_no_transitions(self):
        self.nfa.start_state = 'q1'
        self.nfa.transitions = {}
        self.nfa.accept_states = ['q2']
        self.assertFalse(self.nfa.is_accepted('0'))  # Assuming no transitions is not accepted

    def test_is_rejected_no_accept_states(self):
        self.nfa.start_state = 'q1'
        self.nfa.transitions = {('q1', '0'): ['q2'], ('q1', '1'): ['q1']}
        self.nfa.accept_states = []
        self.assertFalse(self.nfa.is_accepted('0'))

    def test_is_rejected_long_string(self):
        self.nfa.start_state = 'q1'
        self.nfa.transitions = {('q1', '0'): ['q2'], ('q1', '1'): ['q1']}
        self.nfa.accept_states = ['q2']
        self.assertFalse(self.nfa.is_accepted('000000'))
