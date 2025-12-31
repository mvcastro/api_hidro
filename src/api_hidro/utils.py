from typing import Sequence


def flatten_concatenation[T](matrix: Sequence[Sequence[T]]) -> list[T]:
    flat_list: list[T] = []
    for row in matrix:
        flat_list += row
    return flat_list
