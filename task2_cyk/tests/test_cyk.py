from source.cyk import CYK, CNF


def check(grammar, derived, not_derived):
    assert all(map(lambda word: CYK.check_word(grammar, word), derived))
    assert all(map(lambda word: not CYK.check_word(grammar, word), not_derived))


def test_cyk():
    directory = './tests/test_files/'
    path = f'{directory}/test{1}.cnf'
    grammar = CNF()
    grammar.read(path)
    derived = ["a", "ac", "cac", "ccac", "cccac", "EPS"]
    not_derived = ["b", "ab", "abc", "bca", "ca", "c", "ccacc", "caccc"]
    check(grammar, derived, not_derived)
    grammar.read(f'{directory}/test{2}.cnf')
    derived.pop()
    not_derived.append("EPS")
    check(grammar, derived, not_derived)
