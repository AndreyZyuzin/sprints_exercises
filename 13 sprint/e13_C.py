"""Задача C спринта 13.

Подпоследовательность.
Гоша любит играть в игру «Подпоследовательность»: даны 2 строки,
и нужно понять, является ли первая из них подпоследовательностью второй.
Когда строки достаточно длинные, очень трудно получить ответ на этот вопрос,
просто посмотрев на них. Помогите Гоше написать функцию,
которая решает эту задачу..
"""


def input_data():
    """Получение исходные данные."""
    return input(), input()


def is_in_sequence(subsequence, sequence):
    """Определение входит подпоследовние в заданную последование."""
    k_char = 0
    for char in sequence:
        if subsequence[k_char] == char:
            k_char += 1
            if k_char >= len(subsequence):
                return True
    return False


def main():
    subsequence, sequence = input_data()
    print(str(is_in_sequence(subsequence, sequence)))


if __name__ == '__main__':
    main()
