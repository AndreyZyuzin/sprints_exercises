import pytest
from exersices_A import broken_search


class Test_exersices:
    """Тестируем задачу."""

    def test_broken_search(self):
        """Проверка правильного результата."""
        arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
        assert broken_search(arr, 5) == 6
        assert broken_search(arr, 19) == 0
        assert broken_search(arr, 21) == 1
        assert broken_search(arr, 100) == 2
        assert broken_search(arr, 101) == 3
        assert broken_search(arr, 1) == 4
        assert broken_search(arr, 4) == 5
        assert broken_search(arr, 7) == 7
        assert broken_search(arr, 12) == 8
        assert broken_search(arr, 13) == -1
