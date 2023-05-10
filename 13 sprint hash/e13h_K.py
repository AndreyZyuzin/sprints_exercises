"""Задача K спринта 13 hash.

Ближайшая остановка.
Гоша едет в гости к друзьям. Ему придётся сначала ехать на метро,
а потом пересаживаться на автобус. Гоша не любит долго ждать,
поэтому хочет выбрать такую станцию метро, рядом с которой расположено
как можно больше остановок автобуса. Гоша считает, что остановка находится
рядом с метро, если расстояние между ними не превосходит 20 метров.
Обратите внимание, что в одной точке могут располагаться несколько остановок.

Гоше известны все координаты автобусных остановок и координаты
выходов из метро. Помогите ему найти выход из метро,
рядом с которым расположено больше всего остановок.

Напомним, что расстояние между двумя точками с координатами
x1, y1 и x2, y2 вычисляется по формуле sqrt( (x1 - x2)^2 + (y1 - y2)^2 ).
"""
DISTANCE2_MIN = 20*20

def input_data():
    """Получение исходные данные."""
    tmp = int(input())
    array1 = []
    for _ in range(tmp):
        x, y = map(int, input().split())
        array1.append((x, y))
    tmp = int(input())
    array2 = []
    for _ in range(tmp):
        x, y = map(int, input().split())
        array2.append((x, y))
    return array1, array2


def distance2(point1, point2) -> int:
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2


def get_list_suitable_metro(metro, bus):
    arr = [0] * len(metro)
    max_out = 0
    for metro_i, metro_value in enumerate(metro):
        for bus_value in bus:
            if distance2(metro_value, bus_value) <= DISTANCE2_MIN:
                arr[metro_i] += 1
    result = 1
    print('arr: ', arr)
    for item in range(1, len(arr)):
        if arr[item] > arr[result]:
            result = item
    return result + 1


def main():
    metro, bus = input_data()
    print(metro, bus)
    result = get_list_suitable_metro(metro, bus)
    print(result)


if __name__ == '__main__':
    main()
