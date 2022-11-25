class ContextFreeGrammar:
    class BaseState:
        def __init__(self, symbol, index):
            self.symbol = symbol
            self.index = index

        def __hash__(self):
            return self.index

        def __eq__(self, other):
            if isinstance(self, ContextFreeGrammar.State) != \
                    isinstance(other, ContextFreeGrammar.State) or self.index != other.index:
                return False
            return True

    class State(BaseState):
        def __init__(self, symbol, index=0):
            super().__init__(symbol, index)
            self.transitions = set()

        def __hash__(self):
            return self.index

    eps_name = "EPS"
    start = 0
    alphabet_size = 0
    states = []

    def parse_alphabet(self, alphabet_string, symbol_ids):
        alphabet = list(alphabet_string.rstrip("\n").split(": ")[1])
        alphabet.append(self.eps_name)
        self.alphabet_size = len(alphabet)
        for i in range(len(alphabet)):
            self.states.append(self.BaseState(alphabet[i], len(self.states)))
            symbol_ids[alphabet[i]] = self.states[-1]

    def parse_not_terminal(self, not_terminal_string, symbol_ids):
        not_terminal = not_terminal_string.rstrip("\n").split(" & ")
        not_terminal[0] = not_terminal[0].split(": ")[1]
        for state in not_terminal:
            self.states.append(self.State(state, len(self.states)))
            symbol_ids[state] = self.states[-1]

    def parse_start(self, start_string, symbol_ids):
        start_name = start_string.rstrip("\n").split(": ")[-1]
        self.start = symbol_ids[start_name]

    def parse_transition(self, transition_string, symbol_ids):
        start, end = transition_string.rstrip("\n").split(" -> ")
        start_state = symbol_ids[start]
        children = end.split(" & ")
        transition = []
        for child in children:
            child_state = symbol_ids[child]
            transition.append(child_state)
        start_state.transitions.add(tuple(transition))

    def read(self, filename):
        self.states.clear()
        with open(filename, mode="r") as f:
            symbol_ids = dict()
            self.parse_alphabet(f.readline(), symbol_ids)
            self.parse_not_terminal(f.readline(), symbol_ids)
            self.parse_start(f.readline(), symbol_ids)
            transitions_strings = f.readlines()
            for i in range(len(transitions_strings)):
                self.parse_transition(transitions_strings[i], symbol_ids)


class CNF(ContextFreeGrammar):
    def read(self, filename):
        super().read(filename)