from __future__ import annotations

from automates.one_letter_NFA import OneLetterNFA, NFA


class CDFA(NFA):
    def __init__(self, nfa: NFA = None):
        if isinstance(nfa, CDFA):
            super().__init__(nfa)
        else:
            super().__init__()
            if isinstance(nfa, OneLetterNFA):
                self.__build_cdfa(nfa)
            elif nfa is not None:
                self.__build_cdfa(OneLetterNFA(nfa))

    def read_file(self, file_name):
        one_letter_nfa = OneLetterNFA()
        one_letter_nfa.read_file(file_name)
        self.__build_cdfa(one_letter_nfa)

    def __build_cdfa(self, one_letter_nfa: OneLetterNFA):
        self._alphabet = one_letter_nfa._alphabet.copy()
        states_names = dict()
        if len(one_letter_nfa._states_list) == 0:
            return
        reachable_states = [frozenset({one_letter_nfa._states_list[0].name})]
        self._states_list.append(self.State(len(self._states_list), one_letter_nfa._states_list[0].is_terminal))
        states_names[reachable_states[0]] = self._states_list[-1]

        # states_names - by set of states' names in one_letter_nfa get state in cdfa
        # reachable_states - whose children were not processed
        # in _states_list of cdfa values of dicts edges are numbers, while in nfa they are sets
        # bfs

        while len(reachable_states) != 0:
            ids_state = reachable_states.pop()
            state = states_names[ids_state]
            for word in self._alphabet:
                child_set = set()
                # get all children
                for sub_state in ids_state:
                    if word in one_letter_nfa._states_list[sub_state].edges:
                        child_set |= set(map(lambda s: s.name, one_letter_nfa._states_list[sub_state].edges[word]))
                frozen_child = frozenset(child_set)
                # check if already have this state
                if frozen_child not in states_names:
                    self._states_list.append(self.State(len(self._states_list), any(
                        one_letter_nfa._states_list[i].is_terminal for i in frozen_child)))
                    states_names[frozen_child] = self._states_list[-1]
                    reachable_states.append(frozen_child)
                state.edges[word] = states_names[frozen_child]

    def _get_state_string(self, state: CDFA.State):
        # in _states_list of cdfa values of dicts edges are numbers, while in nfa they are sets
        transitions = []
        for word, child in state.edges.items():
            transitions.append(f'-> {word} {child.name}\n')
        return f'State: {state.name}\n{"".join(transitions)}'

    def check_isomorphic(self, other: CDFA) -> bool:
        # bfs check that languages are equal
        if self._alphabet != other._alphabet:
            return False
        stack = [(self._states_list[0], other._states_list[0])]
        for state in self._states_list:
            state.color = 0
        for state in other._states_list:
            state.color = 0
        while len(stack) != 0:
            state_self, state_other = stack.pop()
            if state_self.is_terminal ^ state_other.is_terminal:
                return False
            if state_self.color == 0 or state_other.color == 0:
                state_self.color = 1
                state_other.color = 1
                for word in self._alphabet:
                    stack.append((state_self.edges[word], state_other.edges[word]))
        return True

    def check_equal(self, other: CDFA):
        # check that languages and number of states are equal
        return len(self._states_list) == len(other._states_list) and self.check_isomorphic(other)
