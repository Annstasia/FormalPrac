import pytest
from automates.min_CDFA import MinCDFA, CDFA


@pytest.mark.parametrize("test,answer", [
    (f'tests/test_files/test{i}/test.doa', f'tests/test_files/test{i}/ans_mcdfa.doa') for i in range(1, 5)])
def test_min_cdfa(test, answer):
    cdfa = MinCDFA()
    cdfa.read_file(test)
    cdfa1 = CDFA()
    cdfa1.read_file(answer)
    assert cdfa.check_equal(cdfa1)
