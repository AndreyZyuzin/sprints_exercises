import pytest
from e13_D import number_of_satisfied


class Test_13_N:
    """Тестируем задачу."""

    @pytest.mark.parametrize(
        'children, cookies, expected_result',
        [([1, 1, 4, 4, 5, 5, 5, 10, 10, 10], [1, 4, 4, 4, 5, 6, 7, 8, 9], 7),
         ([2, 4, 3, 7, 10, 4, 2, 1, 4], [1, 5, 5, 4, 8, 6, 5], 7),
         ])
    def test_number_of_satisfied(self, children, cookies, expected_result):
        """Проверка правильного результата."""
        assert number_of_satisfied(children, cookies) == expected_result, (
            f'Жадность {children} и печенье {cookies} должен быть '
            f'{expected_result} довольных.')
