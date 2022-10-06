import pytest
from automates.CDFA import CDFA


@pytest.mark.parametrize("test,answer", [
    (f'tests/test_files/test{i}/test.doa', f'tests/test_files/test{i}/ans_cdfa.doa') for i in range(1, 5)])
def test_cdfa(test, answer):
    cdfa = CDFA()
    cdfa.build_from_file(test)
    print(test)
    print(str(cdfa))
    print('\n\n\n\n\n')
    cdfa1 = CDFA()
    cdfa1.build_from_file(answer)
    assert cdfa.check_isomorphic(cdfa1)
