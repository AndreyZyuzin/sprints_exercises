"""Задача F спринта 13 hash.

Анаграммная группировка.
Вася решил избавиться от проблем с произношением и стать певцом. Он обратился
за помощью к логопеду. Тот посоветовал Васе выполнять упражнение, которое
называется анаграммная группировка. В качестве подготовительного этапа нужно
выбрать из множества строк анаграммы.

Анаграммы –— это строки, которые получаются друг из друга перестановкой
символов. Например, строки «SILENT» и «LISTEN» являются анаграммами.

Помогите Васе найти анаграммы.
"""
def input_data():
    _ = input()
    return [my_counter(item) for item in input().split()]


def input_data2():
    _ = input()
    return [''.join(sorted(item)) for item in input().split()]


def get_indexes_anagrams2(array):
    tmp = dict()
    for index, word in enumerate(array):
        h = hash(word)
        if h not in tmp:
            tmp[h] = [index, str(index)]
            continue
        tmp[h][1] += ' ' + str(index)
    result = sorted(tmp.values(), key=lambda x: x[0])
    return '\n'.join(item[1] for item in result)


def get_indexes_anagrams(array):
    text = ''
    for index, item in enumerate(array):
        if item is None:
            continue
        text += str(index)
        for index2, item2 in enumerate(array[index + 1:], start=index + 1):
            if item == item2:
                text += ' ' + str(index2)
                array[index2] = None
        text += '\n'
    return text


def my_counter(word: str) -> dict:
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def output(arrs):
    for item in arrs:
        print(' '.join(map(str, item)))


def test():
    def run1(array):
        return [my_counter(item) for item in array]

    def run2(array):
        return [''.join(sorted(item)) for item in array]

    def run3(array):
        return [(''.join(sorted(item)), index) for index, item in enumerate(array)]

    def wrapper(func, *args, **kwargs):
        def wrapper():
            return func(*args, **kwargs)
        return wrapper

    import timeit

    arr = ['tan', 'eat', 'tea', 'ate', 'nat', 'bat'] * 100
    # import input_F_array1
    # arr_ = input_F_array1.array[:30]
    arr1 = run1(arr)
    arr2 = run2(arr)
    arr3 = run3(arr)

    result = get_indexes_anagrams2(arr2)
    print(result)
    print('='*80)

    K_TIMES = 10000
    wrapped = wrapper(run1, arr)
    print('array to dict => run1: ', timeit.timeit(wrapped, number=K_TIMES))

    wrapped = wrapper(run2, arr)
    print('array to sorter => run2: ', timeit.timeit(wrapped, number=K_TIMES))

    wrapped = wrapper(run3, arr)
    print('array to sorter and index => run3: ', timeit.timeit(wrapped, number=K_TIMES))

    wrapped = wrapper(get_indexes_anagrams, arr1)
    print('get_indexes_anagrams(arr1): ', timeit.timeit(wrapped, number=K_TIMES))

    wrapped = wrapper(get_indexes_anagrams, arr2[:])
    print('get_indexes_anagrams(arr2): ', timeit.timeit(wrapped, number=K_TIMES))

    wrapped = wrapper(get_indexes_anagrams2, arr2)
    print('get_indexes_anagrams2(arr2): ', timeit.timeit(wrapped, number=K_TIMES))

    wrapped = wrapper(my_counter, arr[0])
    print('my_counter: ', timeit.timeit(wrapped, number=K_TIMES))

    wrapped = wrapper(sorted, arr[0])
    print('sorter: ', timeit.timeit(wrapped, number=K_TIMES))


def main():
    array = input_data2()
    print(get_indexes_anagrams2(array))


if __name__ == '__main__':
    test()
