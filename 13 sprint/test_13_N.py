import pytest
from e13_N import merge2


class Test_13_N:
    """Тестируем задачу."""

    @pytest.mark.parametrize(
        'intervals, expected_result',
        [([[7, 8], [7, 8], [2, 3], [6, 10]], [[2, 3], [6, 10]]),
         ([[1, 3], [3, 5], [4, 6], [5, 6], [2, 4], [7, 10]], [[1, 6], [7, 10]]),
         ([[7, 13], [12, 15], [2, 3], [6, 10]], [[2, 3], [6, 15]]),
         ])
    def test_merge(self, intervals, expected_result):
        """Проверка правильного результата."""
        assert merge2(intervals) == expected_result, (
            f'Массив {intervals} должен быть равен {expected_result}.')
