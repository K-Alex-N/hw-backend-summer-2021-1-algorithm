from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    lst_str: list[str] = text.strip().split()
    if not lst_str:
        return None, None

    mn = min(lst_str, key=len)
    mx = max(lst_str, key=len)
    return mn, mx


