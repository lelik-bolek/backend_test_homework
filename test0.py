from typing import Optional


def lower_join(seq: Optional[set]) -> str:
    """Принимает на вход последовательность и создаёт из неё
    строку в нижнем регистре."""
    return ''.join(seq).lower()
