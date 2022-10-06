from automates.min_CDFA import MinCDFA, CDFA


def test_not_isomorphic():
    mcdfa1 = MinCDFA()
    mcdfa1.build_from_file('tests/test_files/test2/test.doa')
    cdfa2 = CDFA()
    cdfa2.build_from_file('tests/test_files/test3/test.doa')
    mcdfa2 = MinCDFA(cdfa2)
    assert not mcdfa1.check_isomorphic(mcdfa2)
    assert cdfa2.check_isomorphic(mcdfa2)
    assert not cdfa2.check_equal(mcdfa2)
