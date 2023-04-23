
def merge(arr: list, left: int, mid: int, right: int) -> list:
    """Два отсортированных массива,
    сливает их в один отсортированный массив.
    """
    k_cells = right - left
    tmp = [None] * k_cells
    k_tmp = 0
    k_left = left
    k_right = mid
    while k_left < mid and k_right < right:
        if arr[k_left] < arr[k_right]:
            tmp[k_tmp] = arr[k_left]
            k_left += 1
        else:
            tmp[k_tmp] = arr[k_right]
            k_right += 1
        k_tmp += 1
    if k_right == right:
        remainder = mid - k_left
        arr[right - remainder:right] = arr[k_left:mid]
    else:
        remainder = right - k_right
    arr[left: right - remainder] = tmp[:-remainder]
    return arr


def merge_sort(arr: list, left: int, right: int) -> None:
    """Разбивает полуинтервал на две половинки и рекурсивно вызывает
    сортировку отдельно для каждой.
    """
    if right - left <= 1:
        return arr

    half = (left + right) // 2
    merge_sort(arr, left, half)
    merge_sort(arr, half, right)
    merge(arr, left, half, right)


def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected
