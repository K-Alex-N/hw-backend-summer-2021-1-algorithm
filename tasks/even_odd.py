__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """

    even = sum(filter(lambda x: x % 2 == 1, arr))
    odd = sum(filter(lambda x: x % 2 == 0, arr))
    if not even:
        return 0
    return odd / even
