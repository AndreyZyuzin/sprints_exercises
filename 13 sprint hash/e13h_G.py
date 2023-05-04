"""Задача G спринта 13 hash.

Соревнование.
Жители Алгосов любят устраивать турниры по спортивному программированию.
Все участники разбиваются на пары и соревнуются друг с другом. А потом два
самых сильных программиста встречаются в финальной схватке, которая состоит
из нескольких раундов. Если в очередном раунде выигрывает первый участник,
в таблицу с результатами записывается 0, если второй, то 1.
Ничьей в раунде быть не может.

Нужно определить наибольший по длине непрерывный отрезок раундов,
по результатам которого суммарно получается ничья.
Например, если дана последовательность 0 0 1 0 1 1 1 0 0 0,
то раунды с 2-го по 9-й (нумерация начинается с единицы) дают ничью.
"""
def input_data():
    _ = input()
    return input()

def get_length_series(line: str):
    """Получить длину макс серию, в которой равно побед и поражнеий.

    Алгоритм:
    - делаем динамику очков. Наша задача найти крайние игры, после которых
        равное количество очков.
    - делаем проход и фиксируем очки в словарь. также отмечаем тур.
    - делаем проход словаря ищем макс разницы от последнего до первого тура.
    """
    array = line.split()
    scores = [0] * (len(array) + 1)
    for index, item in enumerate(array):
        if array[index] == '1':
            scores[index+1] = scores[index] + 1
        else:
            scores[index+1] = scores[index] - 1

    tours = {}
    for index, value in enumerate(scores):
        if value in tours:
            tours[value][1] = index
        else:
            tours[value] = [index, index]

    result = 0
    for key, values in tours.items():
        if values[1] - values[0] > result:
            result = values[1] - values[0]
    return result


def test():
    line = '0 0 1 0 1 1 1 0 0 0'  # 8
    print(get_length_series(line))


def main():
    line = input_data()
    print(get_length_series(line))


if __name__ == '__main__':
    main()
