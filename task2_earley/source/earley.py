from source.grammar import ContextFreeGrammar


class Earley:
    class EarleyState:
        def __init__(self, dot_pos, transition, left_in_group):
            self.dot = dot_pos
            self.transition = transition
            self.left_counter = left_in_group

        def after_dot(self):
            if self.dot == len(self.transition[1]):
                return None
            return self.transition[1][self.dot]

        def __key(self):
            return self.dot, self.transition, self.left_counter

        def __hash__(self):
            return hash(self.__key())

        def __eq__(self, other):
            return self.__key() == other.__key()

    @staticmethod
    def check_word(grammar: ContextFreeGrammar, word):
        situations_count = len(word) + 1 if word != grammar.eps_name else 1
        dp = [set() for _ in range(situations_count)]
        new_start = grammar.State("S1", -1)
        new_start.transitions.add(tuple([grammar.start]))
        dp[0].add(Earley.EarleyState(0, tuple([new_start, tuple([grammar.start])]), 0))

        for j in range(situations_count):
            old_size = -1
            while old_size != len(dp[j]):
                old_size = len(dp[j])
                Earley.complete(dp, j, grammar)
                Earley.predict(dp, j)
            Earley.scan(dp, j, word)
        for situation in dp[-1]:
            if situation.transition[0] == new_start and situation.dot == 1 and situation.left_counter == 0:
                return True
        return False

    @staticmethod
    def predict(dp, j):
        dp_j = dp[j].copy()
        for situation in dp_j:
            state = situation.after_dot()
            if state is not None and isinstance(state, ContextFreeGrammar.State):
                for child_transition in state.transitions:
                    dp[j].add(Earley.EarleyState(0, tuple([state, child_transition]), j))

    @staticmethod
    def scan(dp, j, word):
        if j == len(dp) - 1:
            return
        dp_j = dp[j].copy()
        for transition in dp_j:
            state = transition.after_dot()
            if state is not None and not isinstance(state, ContextFreeGrammar.State):
                if state.symbol == word[j]:
                    dp[j + 1].add(
                        Earley.EarleyState(transition.dot + 1, transition.transition, transition.left_counter))

    @staticmethod
    def complete(dp, j, grammar):
        dp_j = dp[j].copy()
        for transition in dp_j:
            state = transition.after_dot()
            if state is None or state.symbol == grammar.eps_name:
                dp_parent = dp[transition.left_counter].copy()
                for parent_transition in dp_parent:
                    if parent_transition.after_dot() == transition.transition[0]:
                        dp[j].add(Earley.EarleyState(
                            parent_transition.dot + 1, parent_transition.transition,
                            parent_transition.left_counter
                        ))
