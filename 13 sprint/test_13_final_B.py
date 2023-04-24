import pytest
from exersices_B import is_more


class Test_exersices:
    """Тестируем задачу."""

    @pytest.mark.parametrize(
        'person_1, person_2, expected_result',
        [({'name': 'alla', 'n_exersices': 4, 'penalty': 100},
          {'name': 'gena', 'n_exersices': 6, 'penalty': 1000},
          False),
         ({'name': 'alla', 'n_exersices': 14, 'penalty': 100},
          {'name': 'gena', 'n_exersices': 6, 'penalty': 1000},
          True),
         ({'name': 'alla', 'n_exersices': 6, 'penalty': 100},
          {'name': 'gena', 'n_exersices': 6, 'penalty': 1000},
          True),
         ({'name': 'alla', 'n_exersices': 6, 'penalty': 100},
          {'name': 'gena', 'n_exersices': 6, 'penalty': 10},
          False),
         ({'name': 'alla', 'n_exersices': 6, 'penalty': 100},
          {'name': 'gena', 'n_exersices': 6, 'penalty': 100},
          True), ])
    def test_is_more(self, person_1, person_2, expected_result):
        """Проверка правильного результата."""
        assert is_more(person_1, person_2) == expected_result, (
            f'{person_1} и {person_2} должен быть '
            f'{"сначала" if expected_result else "в конце"}.')
