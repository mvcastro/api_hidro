from typing import get_args
from api_hidro.types import Bacia, Estado


ESTADOS: list[Estado] = list(get_args(Estado))
BACIAS: list[Bacia] = [
    {"Nome_Bacia": "RIO AMAZONAS", "codigobacia": 1},
    {"Nome_Bacia": "RIO TOCANTINS", "codigobacia": 2},
    {"Nome_Bacia": "ATLÂNTICO,TRECHO NORTE/NORDESTE", "codigobacia": 3},
    {"Nome_Bacia": "RIO SÃO FRANCISCO", "codigobacia": 4},
    {"Nome_Bacia": "ATLÂNTICO,TRECHO LESTE", "codigobacia": 5},
    {"Nome_Bacia": "RIO PARANÁ", "codigobacia": 6},
    {"Nome_Bacia": "RIO URUGUAI", "codigobacia": 7},
    {"Nome_Bacia": "ATLÂNTICO, TRECHO SUDESTE", "codigobacia": 8},
    {"Nome_Bacia": "OUTRAS", "codigobacia": 9},
]
