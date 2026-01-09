from typing import Literal, TypedDict

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
    "AR",  # Argentina
    "BO",  # Bolivia
    "CH",  # Chile
    "CO",  # Colombia
    "EQ",  # Equador
    "GF",  # Guiana Francesa
    "GU",  # Guiana
    "PG",  # Paraguai
    "PU",  # Peru
    "SU",  # Suriname
    "UR",  # Uruguay
    "VE",  # Venezuela
]


type CampoInventario = Literal[
    "Altitude",
    "Area_Drenagem",
    "Bacia_Nome",
    "Codigo_Adicional",
    "Codigo_Operadora_Unidade_UF",
    "Data_Periodo_Climatologica_Fim",
    "Data_Periodo_Climatologica_Inicio",
    "Data_Periodo_Desc_Liquida_Fim",
    "Data_Periodo_Desc_liquida_Inicio",
    "Data_Periodo_Escala_Fim",
    "Data_Periodo_Escala_Inicio",
    "Data_Periodo_Piezometria_Fim",
    "Data_Periodo_Piezometria_Inicio",
    "Data_Periodo_Pluviometro_Fim",
    "Data_Periodo_Pluviometro_Inicio",
    "Data_Periodo_Qual_Agua_Fim",
    "Data_Periodo_Qual_Agua_Inicio",
    "Data_Periodo_Registrador_Chuva_Fim",
    "Data_Periodo_Registrador_Chuva_Inicio",
    "Data_Periodo_Registrador_Nivel_Fim",
    "Data_Periodo_Registrador_Nivel_Inicio",
    "Data_Periodo_Sedimento_Inicio",
    "Data_Periodo_Sedimento_fim",
    "Data_Periodo_Tanque_Evapo_Fim",
    "Data_Periodo_Tanque_Evapo_Inicio",
    "Data_Periodo_Telemetrica_Fim",
    "Data_Periodo_Telemetrica_Inicio",
    "Data_Ultima_Atualizacao",
    "Estacao_Nome",
    "Latitude",
    "Longitude",
    "Municipio_Codigo",
    "Municipio_Nome",
    "Operadora_Codigo",
    "Operadora_Sigla",
    "Operadora_Sub_Unidade_UF",
    "Operando",
    "Responsavel_Codigo",
    "Responsavel_Sigla",
    "Responsavel_Unidade_UF",
    "Rio_Codigo",
    "Rio_Nome",
    "Sub_Bacia_Codigo",
    "Sub_Bacia_Nome",
    "Tipo_Estacao",
    "Tipo_Estacao_Climatologica",
    "Tipo_Estacao_Desc_Liquida",
    "Tipo_Estacao_Escala",
    "Tipo_Estacao_Piezometria",
    "Tipo_Estacao_Pluviometro",
    "Tipo_Estacao_Qual_Agua",
    "Tipo_Estacao_Registrador_Chuva",
    "Tipo_Estacao_Registrador_Nivel",
    "Tipo_Estacao_Sedimentos",
    "Tipo_Estacao_Tanque_evapo",
    "Tipo_Estacao_Telemetrica",
    "Tipo_Rede_Basica",
    "Tipo_Rede_Captacao",
    "Tipo_Rede_Classe_Vazao",
    "Tipo_Rede_Curso_Dagua",
    "Tipo_Rede_Energetica",
    "Tipo_Rede_Estrategica",
    "Tipo_Rede_Navegacao",
    "Tipo_Rede_Qual_Agua",
    "Tipo_Rede_Sedimentos",
    "UF_Estacao",
    "UF_Nome_Estacao",
    "codigobacia",
    "codigoestacao",
]

type DictInventarioDaAPI = dict[CampoInventario, str]