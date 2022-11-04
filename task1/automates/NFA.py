from __future__ import annotations

import copy
import typing


class NFA:
    class State:
        name = 0
        edges = dict()

        def __init__(self, new_name, is_terminal=False):
            self.name = new_name
            self.edges = dict()
            self.color = 0
            self.is_terminal = is_terminal

        def __str__(self):
            return str(self.name)

    _EPS = "EPS"
    _states_list: typing.List[NFA.State] = []
    _alphabet: typing.Set[str] = set()

    def __init__(self, nfa: NFA = None):
        if nfa is not None:
            self._states_list = copy.deepcopy(nfa._states_list)
            self._alphabet = copy.deepcopy(nfa._alphabet)
        else:
            self._states_list: typing.List[NFA.State] = []
            self._alphabet: typing.Set[str] = set()

    def build_from_file(self, file_name):
        start_name, acceptance, read_states = self._read_file(file_name)
        self._build_nfa(start_name, acceptance, read_states)

    def __check_state_name(self, state_name, states_names: typing.Dict[object, State]):
        if state_name not in states_names:
            self._states_list.append(self.State(len(self._states_list)))
            states_names[state_name] = self._states_list[-1]
        return states_names[state_name]

    @staticmethod
    def _read_file(file_name):
        start = ""
        read_states: typing.Dict[str, typing.Dict[str, typing.Set[str]]] = dict()
        acceptance: typing.List[str] = []
        with open(file_name, mode="r") as f:
            current_state = ""
            for string in f.readlines():
                string = string.rstrip('\n')
                if string.startswith("Start: "):
                    start = string.split()[1]
                elif string.startswith("Acceptance: "):
                    acceptance = string.lstrip("Acceptance: ").replace(" ", "").split("&")
                elif string.startswith("State: "):
                    current_state = string.split()[1]
                    if current_state not in read_states:
                        read_states[current_state] = dict()
                elif string.startswith("->"):
                    arrow, word, child_state = string.split()
                    read_states[current_state][word] = read_states[current_state].get(word, set()) | {child_state}
        return start, acceptance, read_states

    def _build_nfa(self, start_name, acceptance, read_states):
        if len(read_states) == 0:
            return
        states_names: typing.Dict[str, NFA.State] = dict()
        self._states_list.append(self.State(0))
        states_names[start_name] = self._states_list[0]
        for state_name in acceptance:
            self.__check_state_name(state_name, states_names).is_terminal = True
        for state_name, transitions in read_states.items():
            state = self.__check_state_name(state_name, states_names)
            for word, children in transitions.items():
                state.edges[word] = state.edges.get(word, set()) | set(
                    self.__check_state_name(name, states_names) for name in children)
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
