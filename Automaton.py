from typing import List, Dict


class Automaton:
    def __init__(self):
        # ["q1", "q2]
        self.states: List[str] = []

        # ["0", "1"]
        self.alphabet: List[str] = []

        # {
        #    ("q1", "0"): "q2",
        #    ("q1", "1"): "q1"
        # }
        self.transitions: Dict[(str, str), str] = {}

        # q1
        self.start_state = None

        # ["q2"]
        self.accept_states: List[str] = []

        self.Title = "UNKNOWN AUTOMATON"
        self.TestTitle = "TEST IF STRING IS ACCEPTED OR REJECTED"
        self.TransListTitle = "TRANSITION LIST"
        self.TransTableTitle = "TRANSITION TABLE"

        self.width = 70
        self.singleline = "-" * self.width
        self.doubleline = "=" * self.width

    def print(self):
        print(
            self.singleline + f"\n{self.Title.center(self.width)}\n{self.TransListTitle.center(self.width)}\n" + self.singleline)
        for state in self.states:
            for symbol in self.alphabet:
                key = (state, symbol)
                dest = self.transitions.get(key)
                if dest is None:
                    dest_str = "none"
                else:
                    dest_str = ",".join(dest)
                printlist = f"{'':<1}δ({state}, {symbol}){'':<3} = {'':<3}{dest_str}"
                print((printlist.center(self.width)))

        print(
            self.singleline + f"\n{self.Title.center(self.width)}\n{self.TransTableTitle.center(self.width)}\n" + self.singleline)

        header = f"{'':<3} | {self.alphabet[0]:<8} |"
        for symbol in self.alphabet[1:]:
            header += f" {symbol:<8} |"
        divider = '-' * len(header)

        print(header.center(self.width))
        print(divider.center(self.width))

        for state in self.states:
            row = f"{state:<3} |"
            for symbol in self.alphabet:
                key = (state, symbol)
                dest = self.transitions.get(key)
                if dest is None:
                    dest_str = "none"
                else:
                    dest_str = ",".join(dest)
                row += f" {dest_str:<8} |"
            print(row.center(self.width))
