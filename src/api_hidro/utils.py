from typing import Sequence

import pandas as pd
from pydantic import BaseModel


def flatten_concatenation[T](matrix: Sequence[Sequence[T]]) -> list[T]:
    flat_list: list[T] = []
    for row in matrix:
        flat_list += row
    return flat_list


def as_dataframe(hidro_serie: Sequence[BaseModel] | Sequence[dict]) -> pd.DataFrame:
    serie: list[dict] = []

    for item in hidro_serie:
        if isinstance(item, BaseModel):
            serie.append(item.model_dump())
        elif isinstance(item, dict):
            serie.append(item)
        else:
            raise TypeError(f"Unsupported type: {type(item)}")

    return pd.DataFrame(serie)
