from automates.CDFA import CDFA


class MinCDFA(CDFA):
    def __init__(self, nfa=None):
        super().__init__(nfa)
        if not isinstance(nfa, MinCDFA):
            self.__build_min_cdfa()

    def read_file(self, file_name):
        super().read_file(file_name)
        self.__build_min_cdfa()

    def __build_min_cdfa(self):
        for state in self._states_list:
            if state.is_terminal:
                state.color = 1
            else:
                state.color = 0
        # colors_dicts by state's and it's children classes(colors) get new class
        # in name save current class, in color - future
        while True:
            any_change = False
            for state in self._states_list:
                any_change |= (state.name != state.color)
                state.name = state.color
            if not any_change:
                break
            colors_dict = {}
            free_color = 0
            for state in self._states_list:
                children = state.name, tuple(state.edges[word].name for word in self._alphabet)
                state.color = colors_dict.get(children, free_color)
                if state.color == free_color:
                    colors_dict[children] = state.color
                    free_color += 1
        # each new color is greater than previous. Save in colors representative of each class
        colors = []
        for state in self._states_list:
            if state.name == len(colors):
                colors.append(state)
        self._states_list = colors
        # change each child to representative of child's class
        for state in self._states_list:
            for word, child in state.edges.items():
                state.edges[word] = colors[child.name]
