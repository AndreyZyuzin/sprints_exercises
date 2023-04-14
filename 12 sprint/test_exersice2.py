import pytest
from exersice2 import Stack, StackError, calculator, get_elements


class TestCalculator:
    """Тестируем стек."""

    @pytest.mark.parametrize(
        'line, expected_result',
        [('10 2 4 * +', 18),
         ('-4 4 +', 0),
         ('4 2 * 4 / 25 * 2 - 12 / 1000 + 2 / -999 +', -497),
         ])
    def test_calculator_good(self, line, expected_result):
        """Проверка правильного результата."""
        assert calculator(get_elements(line)) == expected_result, (
            f'Список {line} должен быть равен {expected_result}.'
        )


class TestStack:
    """Тестируем стек."""

    @pytest.mark.parametrize('value', [1, 100, -5, 0])
    def test_get_item_from_stack_use_append(self, value):
        """При добавлении элемента и получение правильный результат."""
        stack = Stack(1)
        stack.append(value)
        assert stack.pop() == value, ('В стек добавлен элемент, '
                                      'после получения вернулся другой.')

    @pytest.mark.parametrize('value', [1, 100, -5, 0])
    def test_get_item_from_stack_use_push(self, value):
        """При добавлении элемента и получение правильный результат."""
        stack = Stack(1)
        stack.push(value)
        assert stack.pop() == value, ('В стек добавлен элемент,'
                                      'после получения вернулся другой.')

    def test_get_item_from_epmty_stack(self):
        """Попытке взять элемент из пустого стека приводит к ошибке."""
        stack = Stack(1)
        with pytest.raises(StackError):
            stack.pop()

    @pytest.mark.parametrize('size', [1, 5])
    def test_increase_size(self, size):
        """Тестирование увеличения стека при наполнении."""
        stack = Stack(size)
        assert stack._Stack__max_size == size
        # откуда мы знаем какая реализация?
        assert len(stack._Stack__items) == size
        for _ in range(size):
            stack.append(1)
        stack.append(2)
        assert stack._Stack__max_size == size * 2
        assert len(stack._Stack__items) == size * 2
        assert stack.pop() == 2
