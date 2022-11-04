import pytest

from automates.NFA import NFA


@pytest.fixture
def nfa():
    nfa = NFA()
    nfa.build_from_file("tests/test_files/test1/test.doa")
    return nfa


def test_read(nfa):
    assert len(nfa._states_list) == 2
    assert nfa._alphabet == {"a", "b"}
    assert set(nfa._states_list[0].edges.keys()) == {"a", "ab", "ba", "b", "EPS"}
    assert nfa._states_list[0].edges["a"] == {nfa._states_list[0]}
    assert nfa._states_list[0].edges["ab"] == {nfa._states_list[0]}
    assert nfa._states_list[0].edges["ba"] == {nfa._states_list[1]}
    assert nfa._states_list[0].edges["b"] == {nfa._states_list[1]}
    assert nfa._states_list[0].edges["EPS"] == {nfa._states_list[1]}
    assert list(nfa._states_list[1].edges.keys()) == []
    assert not nfa._states_list[0].is_terminal
    assert nfa._states_list[1].is_terminal


def test_print(nfa):
    with open("tests/test_files/test1/ans_nfa.doa") as f:
        assert str(nfa).strip("\n") == f.read().strip("\n")
