from automates.min_CDFA import MinCDFA, CDFA
from automates.one_letter_NFA import OneLetterNFA, NFA


def test_transformations():
    nfa = NFA()
    nfa.read_file('tests/test_files/test2/test.doa')
    olnfa = OneLetterNFA(nfa)
    cdfa = CDFA(olnfa)
    min_cdfa = MinCDFA(cdfa)
    answer = MinCDFA()
    answer.read_file('tests/test_files/test2/ans_mcdfa.doa')
    assert min_cdfa.check_equal(answer)
