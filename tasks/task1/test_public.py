import pytest

from .task import task1


class Case:
    def __init__(self, name: str, n: int, m: int, fields: list, areas: list,
                 answer: list):
        self._name = name
        self.n = n
        self.m = m
        self.fields = fields
        self.areas = areas
        self.answer = answer

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        n=3,
        m=3,
        fields=[(0, 0), (1, 1), (2, 3)],
        areas=[((0, 0), (4, 4)), ((0, 0), (2, 2)), ((1, 1), (3, 3))],
        answer=[3, 2, 2],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = task1(
        n=case.n,
        m=case.m,
        fields=case.fields,
        areas=case.areas,
    )
    assert len(answer) == len(case.answer)
    for i in range(len(answer)):
        assert answer[i] == case.answer[i]
