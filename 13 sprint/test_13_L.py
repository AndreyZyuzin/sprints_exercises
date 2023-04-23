import pytest
from e13_L import (line_to_list, search_first_value_and_more,
                   search_first_value_and_more_2)


class Test_13_L:
    """Тестируем стек."""

    @pytest.mark.parametrize('func', [search_first_value_and_more,
                                      search_first_value_and_more_2])
    @pytest.mark.parametrize(
        'line, value, expected_result',
        [('1 2 4 4 6 8', 3, (3, 5)),
         ('1 2 4 4 4 4', 3, (3, -1))
         ])
    def test_search_first_value_and_more(self, func,
                                         line, value, expected_result):
        """Проверка правильного результата."""
        result = (func(line_to_list(line), value),
                  func(line_to_list(line), value * 2))
        assert result == expected_result, (f'Список {line} должен быть равен '
                                           f'{expected_result}.')
