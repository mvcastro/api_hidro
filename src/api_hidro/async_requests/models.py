from datetime import date
from typing import Literal, TypedDict

from api_hidro.types import CodigoBacia, Estado


class Inventario(TypedDict):
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
    Operando: Literal[0, 1]
    Responsavel_Codigo: int
    Responsavel_Sigla: str
    Responsavel_Unidade_UF: int
    Rio_Codigo: int | None
    Rio_Nome: str
    Sub_Bacia_Codigo: int
    Sub_Bacia_Nome: str
    Tipo_Estacao: Literal["Pluviometrica", "Fluviometrica"]
    Tipo_Estacao_Climatologica: Literal[0, 1]
    Tipo_Estacao_Desc_Liquida: Literal[0, 1]
    Tipo_Estacao_Escala: Literal[0, 1]
    Tipo_Estacao_Piezometria: Literal[0, 1]
    Tipo_Estacao_Pluviometro: Literal[0, 1]
    Tipo_Estacao_Qual_Agua: Literal[0, 1]
    Tipo_Estacao_Registrador_Chuva: Literal[0, 1]
    Tipo_Estacao_Registrador_Nivel: Literal[0, 1]
    Tipo_Estacao_Sedimentos: Literal[0, 1]
    Tipo_Estacao_Tanque_evapo: Literal[0, 1]
    Tipo_Estacao_Telemetrica: Literal[0, 1]
    Tipo_Rede_Basica: Literal[0, 1]
    Tipo_Rede_Captacao: Literal[0, 1]
    Tipo_Rede_Classe_Vazao: Literal[0, 1]
    Tipo_Rede_Curso_Dagua: Literal[0, 1]
    Tipo_Rede_Energetica: Literal[0, 1]
    Tipo_Rede_Estrategica: Literal[0, 1]
    Tipo_Rede_Navegacao: Literal[0, 1]
    Tipo_Rede_Qual_Agua: Literal[0, 1]
    Tipo_Rede_Sedimentos: Literal[0, 1]
    UF_Estacao: Estado
    UF_Nome_Estacao: str
    codigobacia: CodigoBacia
    codigoestacao: int
