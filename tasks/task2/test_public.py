import pytest

from .task import task2


class Case:
    def __init__(self, name: str, n: int, mans: list, answer: list):
        self._name = name
        self.n = n
        self.mans = mans
        self.answer = answer

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        n=5,
        mans=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
        answer=[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = task2(
        n=case.n,
        mans=case.mans,
    )

    assert len(answer) == len(case.answer)
    for i in range(len(answer)):
        assert answer[i][0] == case.answer[i][0]
        assert answer[i][1] == case.answer[i][1]
