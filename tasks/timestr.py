__all__ = (
    'seconds_to_str',
)

from math import floor


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    d = floor(seconds / (24 * 60 * 60))
    h = floor(seconds / (60 * 60) % 24)
    m = floor(seconds / 60 % 60)
    s = seconds % 60

    d_str = f'{d:02}d'
    h_str = f'{h:02}h'
    m_str = f'{m:02}m'
    s_str = f'{s:02}s'

    if d:
        return d_str + h_str + m_str + s_str
    elif h:
        return h_str + m_str + s_str
    elif m:
        return m_str + s_str
    else:
        return s_str
