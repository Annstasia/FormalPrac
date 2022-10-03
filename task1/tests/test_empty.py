from automates.min_CDFA import MinCDFA

empty = """DOA: v1
Start: 
Acceptance: 
--BEGIN--
--END--"""


def test_empty():
    mcdfa = MinCDFA()
    mcdfa.read_file("tests/test_files/test5/test.doa")
    assert str(mcdfa) == empty
