from datetime import date, datetime
from typing import Literal, TypedDict

from api_hidro.data_types import CodigoBacia, Estado

type JSONObjectValues = int | str | float | bool | None
type JSONObject = dict[str, JSONObjectValues]
type JSONList = list[JSONObject]


class JSONAPIResponse(TypedDict):
    status: str
    code: int
    message: str
    items: JSONList


class InventarioDaAPI(TypedDict):
    Altitude: float | None
    Area_Drenagem: float | None
    Bacia_Nome: str
    Codigo_Adicional: str | None
    Codigo_Operadora_Unidade_UF: int | None
    Data_Periodo_Climatologica_Fim: date | None
    Data_Periodo_Climatologica_Inicio: date | None
    Data_Periodo_Desc_Liquida_Fim: date | None
    Data_Periodo_Desc_liquida_Inicio: date | None
    Data_Periodo_Escala_Fim: date | None
    Data_Periodo_Escala_Inicio: date | None
    Data_Periodo_Piezometria_Fim: date | None
    Data_Periodo_Piezometria_Inicio: date | None
    Data_Periodo_Pluviometro_Fim: date | None
    Data_Periodo_Pluviometro_Inicio: date | None
    Data_Periodo_Qual_Agua_Fim: date | None
    Data_Periodo_Qual_Agua_Inicio: date | None
    Data_Periodo_Registrador_Chuva_Fim: date | None
    Data_Periodo_Registrador_Chuva_Inicio: date | None
    Data_Periodo_Registrador_Nivel_Fim: date | None
    Data_Periodo_Registrador_Nivel_Inicio: date | None
    Data_Periodo_Sedimento_Inicio: date | None
    Data_Periodo_Sedimento_fim: date | None
    Data_Periodo_Tanque_Evapo_Fim: date | None
    Data_Periodo_Tanque_Evapo_Inicio: date | None
    Data_Periodo_Telemetrica_Fim: date | None
    Data_Periodo_Telemetrica_Inicio: date | None
    Data_Ultima_Atualizacao: date | None
    Estacao_Nome: str
    Latitude: float
    Longitude: float
    Municipio_Codigo: int
    Municipio_Nome: str
    Operadora_Codigo: int
    Operadora_Sigla: int
    Operadora_Sub_Unidade_UF: int | None
    Operando: bool
    Responsavel_Codigo: int
    Responsavel_Sigla: str
    Responsavel_Unidade_UF: int
    Rio_Codigo: int | None
    Rio_Nome: str
    Sub_Bacia_Codigo: int
    Sub_Bacia_Nome: str
    Tipo_Estacao: Literal["Pluviometrica", "Fluviometrica"]
    Tipo_Estacao_Climatologica: bool
    Tipo_Estacao_Desc_Liquida: bool
    Tipo_Estacao_Escala: bool
    Tipo_Estacao_Piezometria: bool
    Tipo_Estacao_Pluviometro: bool
    Tipo_Estacao_Qual_Agua: bool
    Tipo_Estacao_Registrador_Chuva: bool
    Tipo_Estacao_Registrador_Nivel: bool
    Tipo_Estacao_Sedimentos: bool
    Tipo_Estacao_Tanque_evapo: bool
    Tipo_Estacao_Telemetrica: bool
    Tipo_Rede_Basica: bool
    Tipo_Rede_Captacao: bool
    Tipo_Rede_Classe_Vazao: bool
    Tipo_Rede_Curso_Dagua: bool
    Tipo_Rede_Energetica: bool
    Tipo_Rede_Estrategica: bool
    Tipo_Rede_Navegacao: bool
    Tipo_Rede_Qual_Agua: bool
    Tipo_Rede_Sedimentos: bool
    UF_Estacao: Estado
    UF_Nome_Estacao: str
    codigobacia: CodigoBacia
    codigoestacao: int


class DadoDiarioVazaoDaAPI(TypedDict):
    codigoestacao: int
    Data_Hora_Dado: datetime
    Data_Ultima_Alteracao: datetime
    Dia_Maxima: int
    Dia_Minima: int
    Maxima: float
    Maxima_Status: float
    Media: float
    Media_Anual: float | None
    Media_Anual_Status: bool | None
    Media_Status: float
    Mediadiaria: float
    Metodo_Obtencao_Vazoes: int
    Minima: float
    Minima_Status: bool
    Nivel_Consistencia: Literal[1, 2]
    Vazao_01: float | None
    Vazao_02: float | None
    Vazao_03: float | None
    Vazao_04: float | None
    Vazao_05: float | None
    Vazao_06: float | None
    Vazao_07: float | None
    Vazao_08: float | None
    Vazao_09: float | None
    Vazao_10: float | None
    Vazao_11: float | None
    Vazao_12: float | None
    Vazao_13: float | None
    Vazao_14: float | None
    Vazao_15: float | None
    Vazao_16: float | None
    Vazao_17: float | None
    Vazao_18: float | None
    Vazao_19: float | None
    Vazao_20: float | None
    Vazao_21: float | None
    Vazao_22: float | None
    Vazao_23: float | None
    Vazao_24: float | None
    Vazao_25: float | None
    Vazao_26: float | None
    Vazao_27: float | None
    Vazao_28: float | None
    Vazao_29: float | None
    Vazao_30: float | None
    Vazao_31: float | None
    Vazao_01_Status: bool | None
    Vazao_02_Status: bool | None
    Vazao_03_Status: bool | None
    Vazao_04_Status: bool | None
    Vazao_05_Status: bool | None
    Vazao_06_Status: bool | None
    Vazao_07_Status: bool | None
    Vazao_08_Status: bool | None
    Vazao_09_Status: bool | None
    Vazao_10_Status: bool | None
    Vazao_11_Status: bool | None
    Vazao_12_Status: bool | None
    Vazao_13_Status: bool | None
    Vazao_14_Status: bool | None
    Vazao_15_Status: bool | None
    Vazao_16_Status: bool | None
    Vazao_17_Status: bool | None
    Vazao_18_Status: bool | None
    Vazao_19_Status: bool | None
    Vazao_20_Status: bool | None
    Vazao_21_Status: bool | None
    Vazao_22_Status: bool | None
    Vazao_23_Status: bool | None
    Vazao_24_Status: bool | None
    Vazao_25_Status: bool | None
    Vazao_26_Status: bool | None
    Vazao_27_Status: bool | None
    Vazao_28_Status: bool | None
    Vazao_29_Status: bool | None
    Vazao_30_Status: bool | None
    Vazao_31_Status: bool | None


class DadoTelemetricaAdotadaOriginalDaAPI(TypedDict):
    codigoestacao: int
    Chuva_Adotada: float | None
    Chuva_Adotada_Status: bool | None
    Cota_Adotada: float | None
    Cota_Adotada_Status: bool | None
    Data_Atualizacao: datetime
    Data_Hora_Medicao: datetime
    Vazao_Adotada: float | None
    Vazao_Adotada_Status: bool | None


class DadoTelemetricaDetalhadaOriginalDaAPI(TypedDict):
    codigoestacao: int
    Bateria: float | None
    Chuva_Acumulada: float | None
    Chuva_Acumulada_Status: float | None
    Chuva_Adotada: float | None
    Chuva_Adotada_Status: bool | None
    Cota_Adotada: float | None
    Cota_Adotada_Status: bool | None
    Cota_Display: float | None
    Cota_Display_Status: bool | None
    Cota_Manual: float | None
    Cota_Manual_Status: bool | None
    Cota_Sensor: float | None
    Cota_Sensor_Status: bool | None
    Data_Atualizacao: datetime | None
    Data_Hora_Medicao: datetime | None
    Pressao_Atmosferica: float | None
    Pressao_Atmosferica_Status: bool | None
    Temperatura_Agua: float | None
    Temperatura_Agua_Status: bool | None
    Temperatura_Interna: float | None
    Vazao_Adotada: float | None
    Vazao_Adotada_Status: bool | None
