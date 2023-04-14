import pytest
from exersice1 import Deque, Deque2, DequeError


class TestDeque:
    """Тестируем дек."""
    @pytest.mark.parametrize('klass', [Deque, Deque2])
    @pytest.mark.parametrize('values', [(1, 0, -5, 3), (), (1,)])
    def test_to_front_from_front(self, klass, values):
        """При добавить в начало и получить из начала."""
        length = len(values)
        deque = klass(length)
        for item in range(length):
            deque.push_front(values[item])
        for item in range(length):
            response = deque.pop_front()
            value = values[length - 1 - item]
            assert response == value, (
                f'В дек добавлен элемент в начало {value}, '
                f'но вернулся другой {response}.')

    @pytest.mark.parametrize('klass', [Deque, Deque2])
    @pytest.mark.parametrize('values', [(1, 0, -5, 3)])
    def test_to_front_from_back(self, klass, values):
        """При добавить в начало и получить из конца."""
        length = len(values)
        deque = klass(length)
        for item in range(length):
            deque.push_front(values[item])
        for item in range(length):
            response = deque.pop_back()
            value = values[item]
            assert response == value, (
                f'В дек добавлен элемент в начало {value}, '
                f'но вернулся другой {response}.')

    @pytest.mark.parametrize('klass', [Deque, Deque2])
    @pytest.mark.parametrize('values', [(1, 0, -5, 3)])
    def test_to_back_from_back(self, klass, values):
        """При добавить в начало и получить из конца."""
        length = len(values)
        deque = klass(length)
        for item in range(length):
            deque.push_back(values[item])
        for item in range(length):
            response = deque.pop_back()
            value = values[length - 1 - item]
            assert response == value, (
                f'В дек добавлен элемент в начало {value}, '
                f'но вернулся другой {response}.')

    @pytest.mark.parametrize('klass', [Deque, Deque2])
    @pytest.mark.parametrize('values', [(1, 0, -5, 3)])
    def test_to_back_from_front(self, klass, values):
        """При добавить в начало и получить из конца."""
        length = len(values)
        deque = klass(length)
        for item in range(length):
            deque.push_back(values[item])
        for item in range(length):
            response = deque.pop_front()
            value = values[item]
            assert response == value, (
                f'В дек добавлен элемент в начало {value}, '
                f'но вернулся другой {response}.')

    @pytest.mark.parametrize('klass', [Deque, Deque2])
    def test_get_item_from_epmty_deque_front(self, klass):
        """Попытке взять элемент из пустого дека приводит к ошибке."""
        deque = klass(1)
        with pytest.raises(Exception):
            deque.pop_front()

    @pytest.mark.parametrize('klass', [Deque, Deque2])
    def test_get_item_from_epmty_deque_back(self, klass):
        """Попытке взять элемент из пустого дека приводит к ошибке."""
        deque = klass(1)
        with pytest.raises(Exception):
            deque.pop_back()

    @pytest.mark.parametrize('klass', [Deque, Deque2])
    @pytest.mark.parametrize('size', [1, 10, 0])
    def test_put_item_in_deque_front(self, klass, size):
        """Добавить элемент в переполненный дек приводит к ошибке."""
        deque = klass(size)
        for _ in range(size):
            deque.push_back(100)
        with pytest.raises(Exception):
            deque.push_front(1001)

    @pytest.mark.parametrize('klass', [Deque, Deque2])
    @pytest.mark.parametrize('size', [1, 10, 0])
    def test_put_item_in_deque_back(self, klass, size):
        """Добавить элемент в переполненный дек приводит к ошибке."""
        deque = klass(size)
        for _ in range(size):
            deque.push_front(100)
        with pytest.raises(DequeError):
            deque.push_back(1001)
