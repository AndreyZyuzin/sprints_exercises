import pytest
from e13_H import line_to_array, sort, output


class Test_13_H:
    """Тестируем задачу."""

    @pytest.mark.parametrize(
        'line, expected_result',
        [('9 10 1 1 1 6', '9611110'),
         ('82 58 66 34 64 37 40 97 93 52 28 98 90 64 19 22 21 83 56 70 46 17 31 51 55 41 68 18 98 89 88 74 6 6 31 36 35 8', '9898979390898888382747068666664645856555251464140373635343131282221191817'),
         ('9 18 1 65 51 16 6 43 6 36 7 11 64 5 1 76 15 11 11 15 57 95 3 49 92 78 83 51 10 3', '995928378776666564575515149433633181615151111111110'),
         ])
    def test_big_number(self, line, expected_result):
        """Проверка правильного результата."""
        numbers = sort(line_to_array(line))
        assert output(numbers) == expected_result, (
            f'Строка {line} должена быть равен {expected_result}.')
