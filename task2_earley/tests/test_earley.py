from source.earley import ContextFreeGrammar, Earley


def check(grammar, derived, not_derived):
    assert all(map(lambda word: Earley.check_word(grammar, word), derived))
    assert all(map(lambda word: not Earley.check_word(grammar, word), not_derived))


def test_earley():
    derived = [["a", "ac", "cac", "ccac", "cccac", "EPS"],
               ["ab", "aabb", "abab", "aaabbb"]]
    not_derived = [["b", "ab", "abc", "bca", "ca", "c", "ccacc", "caccc"],
                   ["EPS", "a", "b", "aba", "abaabbab"]]
    for i in range(1, 3):
        path = f'./tests/test_files/test{i}.gr'
        grammar = ContextFreeGrammar()
        grammar.read(path)
        check(grammar, derived[i-1], not_derived[i-1])
