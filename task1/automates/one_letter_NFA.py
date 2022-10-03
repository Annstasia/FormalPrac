from automates.NFA import NFA


class OneLetterNFA(NFA):
    def __init__(self, nfa: NFA = None):
        super().__init__(nfa)
        if not isinstance(nfa, OneLetterNFA):
            self.__make_one_letter()

    def read_file(self, file_name):
        super().read_file(file_name)
        self.__make_one_letter()

    def __make_one_letter(self):
        # split words in letters
        previous_length = len(self._states_list)
        for state_number in range(previous_length):
            old_edges = self._states_list[state_number].edges.copy()
            self._states_list[state_number].edges = dict()
            for word in old_edges:
                current_state = self._states_list[state_number]
                if word == self._EPS:
                    current_state.edges[word] = old_edges[word]
                    continue
                for i in range(len(word) - 1):
                    imaginary_state = self.State(len(self._states_list))
                    self._states_list.append(imaginary_state)
                    current_state.edges[word[i]] = current_state.edges.get(word[i], set()) | {
                        imaginary_state}
                    current_state = imaginary_state
                current_state.edges[word[-1]] = current_state.edges.get(word[-1], set()) | old_edges[word]
        self.__delete_eps()

    def __delete_eps(self):
        color = 0
        for state in self._states_list:
            state.color = color
        reachable_states = []
        # for each state find reachable by EPS states
        for parent_state in self._states_list:
            color += 1
            parent_state.color = color
            reachable_states.append(parent_state)
            while len(reachable_states) != 0:
                state = reachable_states.pop()
                for word, children in state.edges.items():
                    if word == self._EPS:
                        for child_state in children:
                            if child_state.color != color:
                                child_state.color = color
                                reachable_states.append(child_state)
                        # if terminal is reachable by EPS mark parent terminal
                        if not parent_state.is_terminal and any(child.is_terminal for child in children):
                            parent_state.is_terminal = True
                    else:
                        # To children of reachable by EPS states add edges from parent state.
                        parent_state.edges[word] = parent_state.edges.get(word, set()) | children
        # now can delete eps
        for state in self._states_list:
            if self._EPS in state.edges:
                del state.edges[self._EPS]
        self.__delete_unused()

    def __delete_unused(self):
        # find reachable from start. Rename and save only them in _states_list
        if len(self._states_list) == 0:
            return
        color = 0
        for state in self._states_list:
            state.color = color
        color += 1
        start = self._states_list[0]
        self._states_list.clear()
        start.color = color
        self._states_list.append(start)
        reachable_states = [start]
        while len(reachable_states) != 0:
            state = reachable_states.pop()
            for children in state.edges.values():
                for child in children:
                    if child.color != color:
                        child.color = color
                        child.name = len(self._states_list)
                        self._states_list.append(child)
                        reachable_states.append(child)
