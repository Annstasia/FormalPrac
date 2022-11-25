from source.grammar import CNF


class CYK:
    @staticmethod
    def check_word(cnf: CNF, word):
        if word == cnf.eps_name:
            for transition in cnf.start.transitions:
                if transition[0].index == cnf.alphabet_size - 1:
                    return True
            return False
        dp = [[[False] * len(cnf.states) for _ in range(len(word))] for _ in range(len(word))]
        for state in cnf.states[cnf.alphabet_size:]:
            for transition in state.transitions:
                if len(transition) == 1:
                    for i in range(len(word)):
                        if word[i] == transition[0].symbol:
                            dp[i][i][state.index] = True
        for delta in range(1, len(word)):
            for i in range(len(word) - delta):
                for t in range(cnf.alphabet_size, len(cnf.states)):
                    for transition in cnf.states[t].transitions:
                        if len(transition) == 2:
                            for k in range(delta):
                                dp[i][i + delta][t] |= dp[i][i + k][transition[0].index] and dp[i + k + 1][i + delta][
                                    transition[1].index]
        return dp[0][len(word) - 1][cnf.start.index]
