import pytest
from e13_C import is_in_sequence


class Test_13_N:
    """Тестируем задачу."""

    @pytest.mark.parametrize(
        'sub, sequence, expected_result',
        [('abc', 'ahbgdcu', True),
         ('abcp', 'ahpc', False),
         ])
    def test_merge(self, sub, sequence, expected_result):
        """Проверка правильного результата."""
        assert is_in_sequence(sub, sequence) == expected_result, (
            f'Подпоследование {sub} не входит в {sequence}.')
