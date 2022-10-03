from automates.one_letter_NFA import OneLetterNFA


def swap_by_index(_states_list, index1, index2):
    t = _states_list[index1]
    _states_list[index1] = _states_list[index2]
    _states_list[index2] = t
    _states_list[index1].name = index1
    _states_list[index2].name = index2


def test_olnfa():
    olnfa = OneLetterNFA()
    olnfa.read_file("tests/test_files/test1/test.doa")
    olnfa._states_list[0].name = 0
    for state in olnfa._states_list[0].edges["a"]:
        if state != olnfa._states_list[0]:
            swap_by_index(olnfa._states_list, 1, state.name)
            state.name = 1
    for state in olnfa._states_list[0].edges["b"]:
        print("b", state.is_terminal, state.name)
        if state.is_terminal:
            swap_by_index(olnfa._states_list, 3, state.name)

        else:
            swap_by_index(olnfa._states_list, 2, state.name)
    with open("tests/test_files/test1/ans_olnfa.doa") as f:
        assert str(olnfa).strip("\n ") == f.read().strip("\n ")
