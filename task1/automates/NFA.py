from __future__ import annotations

import copy


class NFA:
    class State:
        name = 0
        edges = dict()

        def __init__(self, new_name, is_terminal=False):
            self.name = new_name
            self.edges = dict()
            self.color = 0
            self.is_terminal = is_terminal
        #
        # def get_next_state_name(self, letter):
        #     return frozenset(i.name for i in self.edges[letter])

        def __str__(self):
            return str(self.name)

    _EPS = "EPS"
    _states_list: list[NFA.State] = []
    _alphabet: set[str] = set()

    def __init__(self, nfa: NFA = None):
        if nfa is not None:
            self._states_list = copy.deepcopy(nfa._states_list)
            self._alphabet = copy.deepcopy(nfa._alphabet)
        else:
            self._states_list: list[NFA.State] = []
            self._alphabet: set[str] = set()

    def __check_state_name(self, state_name, states_names: dict[object, State]):
        if state_name not in states_names:
            self._states_list.append(self.State(len(self._states_list)))
            states_names[state_name] = self._states_list[-1]
        return states_names[state_name]

    def read_file(self, file_name):
        # read automate and rename states. state's index in _states_list is equal to it name
        states_names: dict[str, NFA.State] = dict()
        with open(file_name, mode="r") as f:
            current_state = None
            for string in f.readlines():
                string = string.rstrip('\n')
                if string.startswith("Start: "):
                    self._states_list.append(self.State(0))
                    states_names[string.split()[1]] = self._states_list[0]
                elif string.startswith("Acceptance: "):
                    states = string.lstrip("Acceptance: ").replace(" ", "").split("&")
                    for state_name in states:
                        self.__check_state_name(state_name, states_names).is_terminal = True
                elif string.startswith("State: "):
                    state_name = string.split()[1]
                    current_state = self.__check_state_name(state_name, states_names)
                elif string.startswith("->"):
                    arrow, word, child_state = string.split()
                    child = self.__check_state_name(child_state, states_names)
                    current_state.edges[word] = current_state.edges.get(word, set()).union({child})
                    if word != self._EPS:
                        self._alphabet |= set(word)

    def _get_state_string(self, state: State):
        transitions = []
        for word, children in state.edges.items():
            for child in children:
                transitions.append(f'-> {word} {child.name}\n')
        transitions.sort()
        return f'State: {state.name}\n{"".join(transitions)}'

    def __str__(self):
        header = f'DOA: v1'
        start = f'Start: '
        if len(self._states_list) != 0:
            start += str(self._states_list[0].name)
        acceptance = []
        begin = "--BEGIN--"
        states = []
        for state in self._states_list:
            if state.is_terminal:
                acceptance.append(str(state.name))
            states.append(self._get_state_string(state))
        end = "--END--"
        return f'{header}\n{start}\nAcceptance: {" & ".join(acceptance)}\n{begin}\n{"".join(states)}{end}'
