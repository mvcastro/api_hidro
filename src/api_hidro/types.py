from typing import Literal, TypedDict

type JSONObjectValues = int | str | float | bool | None
type JSONObject = dict[str, JSONObjectValues]
type JSONList = list[JSONObject]


class JSONAPIResponse(TypedDict):
    status: str
    code: int
    message: str
    items: JSONList


type TipoTelemetrica = Literal["Detalhada", "Adotada"]
type TipoFiltroData = Literal["DATA_LEITURA", "DATA_ULTIMA_ATUALIZACAO"]
type IntervaloDeBusca = Literal[
    "MINUTO_5",
    "MINUTO_10",
    "MINUTO_15",
    "MINUTO_30",
    "HORA_1",
    "HORA_2",
    "HORA_3",
    "HORA_4",
    "HORA_5",
    "HORA_6",
    "HORA_7",
    "HORA_8",
    "HORA_9",
    "HORA_10",
    "HORA_11",
    "HORA_12",
    "HORA_13",
    "HORA_14",
    "HORA_15",
    "HORA_16",
    "HORA_17",
    "HORA_18",
    "HORA_19",
    "HORA_20",
    "HORA_21",
    "HORA_22",
    "HORA_23",
    "HORA_24",
]

type CodigoBacia = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9]


class Bacia(TypedDict):
    Nome_Bacia: str
    codigobacia: CodigoBacia


type Estado = Literal[
    "AC",
    "AL",
    "AM",
    "AP",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
    "TO",
    # Internacionais
    "AR", # Argentina
    "BO", # Bolivia
    "CH", # Chile
    "CO", # Colombia
    "EQ", # Equador
    "GF", # Guiana Francesa
    "GU", # Guiana
    "PG", # Paraguai
    "PU", # Peru
    "SU", # Suriname
    "UR", # Uruguay
    "VE", # Venezuela
]
