from abc import ABC
from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from api_hidro.types import CodigoBacia, Estado


class Inventario(BaseModel):
    altitude: float | None
    area_drenagem: float | None
    bacia_nome: str
    codigo_adicional: str | None
    codigo_operadora_unidade_uf: int | None = Field(alias="Codigo_Operadora_Unidade_UF")
    data_periodo_climatologica_fim: date | None
    data_periodo_climatologica_inicio: date | None
    data_periodo_desc_liquida_fim: date | None
    data_periodo_desc_liquida_inicio: date | None = Field(
        alias="Data_Periodo_Desc_liquida_Inicio"
    )
    data_periodo_escala_fim: date | None
    data_periodo_escala_inicio: date | None
    data_periodo_piezometria_fim: date | None
    data_periodo_piezometria_inicio: date | None
    data_periodo_pluviometro_fim: date | None
    data_periodo_pluviometro_inicio: date | None
    data_periodo_qual_agua_fim: date | None
    data_periodo_qual_agua_inicio: date | None
    data_periodo_registrador_chuva_fim: date | None
    data_periodo_registrador_chuva_inicio: date | None
    data_periodo_registrador_nivel_fim: date | None
    data_periodo_registrador_nivel_inicio: date | None
    data_periodo_sedimento_inicio: date | None
    data_periodo_sedimento_fim: date | None = Field(alias="Data_Periodo_Sedimento_fim")
    data_periodo_tanque_evapo_fim: date | None
    data_periodo_tanque_evapo_inicio: date | None
    data_periodo_telemetrica_fim: date | None
    data_periodo_telemetrica_inicio: date | None
    data_ultima_atualizacao: datetime | None
    estacao_nome: str
    latitude: float
    longitude: float
    municipio_codigo: int
    municipio_nome: str
    operadora_codigo: int
    operadora_sigla: str
    operadora_sub_unidade_uf: int | None = Field(alias="Operadora_Sub_Unidade_UF")
    operando: bool
    responsavel_codigo: int
    responsavel_sigla: str
    responsavel_unidade_uf: int | None = Field(alias="Responsavel_Unidade_UF")
    rio_codigo: int | None
    rio_nome: str
    sub_bacia_codigo: int
    sub_bacia_nome: str
    tipo_estacao: Literal["Pluviometrica", "Fluviometrica"]
    tipo_estacao_climatologica: bool
    tipo_estacao_desc_liquida: bool
    tipo_estacao_escala: bool
    tipo_estacao_piezometria: bool
    tipo_estacao_pluviometro: bool
    tipo_estacao_qual_agua: bool
    tipo_estacao_registrador_chuva: bool
    tipo_estacao_registrador_nivel: bool
    tipo_estacao_sedimentos: bool
    tipo_estacao_tanque_evapo: bool = Field(alias="Tipo_Estacao_Tanque_evapo")
    tipo_estacao_telemetrica: bool
    tipo_rede_basica: bool | None
    tipo_rede_captacao: int | None
    tipo_rede_classe_vazao: int | None
    tipo_rede_curso_dagua: int | None
    tipo_rede_energetica: bool | None
    tipo_rede_estrategica: bool | None
    tipo_rede_navegacao: bool | None
    tipo_rede_qual_agua: int | None
    tipo_rede_sedimentos: bool | None
    uf_estacao: Estado = Field(alias="UF_Estacao")
    uf_nome_estacao: str = Field(alias="UF_Nome_Estacao")
    codigobacia: int = Field(alias="codigobacia", ge=1, le=9)
    codigoestacao: int = Field(alias="codigoestacao")

    model_config = ConfigDict(
        populate_by_name=True, alias_generator=lambda s: s.title()
    )


class InventarioOriginalDaAPI(BaseModel):
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


class _DadoDiario(BaseModel, ABC):
    codigoestacao: int
    data_hora_dado: datetime
    data_ultima_alteracao: datetime
    dia_maxima: int
    dia_minima: int
    maxima: float
    maxima_status: float
    media: float
    media_anual: float | None
    media_anual_status: bool | None
    media_status: float
    mediadiaria: float
    metodo_obtencao_vazoes: int
    minima: float
    minima_status: bool
    nivel_consistencia: int = Field(ge=1, le=2)

    model_config = ConfigDict(
        populate_by_name=True, alias_generator=lambda s: s.title()
    )


class DadosDoMesChuva(_DadoDiario):
    chuva_01: float | None
    chuva_02: float | None
    chuva_03: float | None
    chuva_04: float | None
    chuva_05: float | None
    chuva_06: float | None
    chuva_07: float | None
    chuva_08: float | None
    chuva_09: float | None
    chuva_10: float | None
    chuva_11: float | None
    chuva_12: float | None
    chuva_13: float | None
    chuva_14: float | None
    chuva_15: float | None
    chuva_16: float | None
    chuva_17: float | None
    chuva_18: float | None
    chuva_19: float | None
    chuva_20: float | None
    chuva_21: float | None
    chuva_22: float | None
    chuva_23: float | None
    chuva_24: float | None
    chuva_25: float | None
    chuva_26: float | None
    chuva_27: float | None
    chuva_28: float | None
    chuva_29: float | None
    chuva_30: float | None
    chuva_31: float | None
    chuva_01_status: bool | None
    chuva_02_status: bool | None
    chuva_03_status: bool | None
    chuva_04_status: bool | None
    chuva_05_status: bool | None
    chuva_06_status: bool | None
    chuva_07_status: bool | None
    chuva_08_status: bool | None
    chuva_09_status: bool | None
    chuva_10_status: bool | None
    chuva_11_status: bool | None
    chuva_12_status: bool | None
    chuva_13_status: bool | None
    chuva_14_status: bool | None
    chuva_15_status: bool | None
    chuva_16_status: bool | None
    chuva_17_status: bool | None
    chuva_18_status: bool | None
    chuva_19_status: bool | None
    chuva_20_status: bool | None
    chuva_21_status: bool | None
    chuva_22_status: bool | None
    chuva_23_status: bool | None
    chuva_24_status: bool | None
    chuva_25_status: bool | None
    chuva_26_status: bool | None
    chuva_27_status: bool | None
    chuva_28_status: bool | None
    chuva_29_status: bool | None
    chuva_30_status: bool | None
    chuva_31_status: bool | None

    model_config = ConfigDict(
        populate_by_name=True, alias_generator=lambda s: s.title()
    )


class DadosDoMesCota(_DadoDiario):
    cota_01: float | None
    cota_02: float | None
    cota_03: float | None
    cota_04: float | None
    cota_05: float | None
    cota_06: float | None
    cota_07: float | None
    cota_08: float | None
    cota_09: float | None
    cota_10: float | None
    cota_11: float | None
    cota_12: float | None
    cota_13: float | None
    cota_14: float | None
    cota_15: float | None
    cota_16: float | None
    cota_17: float | None
    cota_18: float | None
    cota_19: float | None
    cota_20: float | None
    cota_21: float | None
    cota_22: float | None
    cota_23: float | None
    cota_24: float | None
    cota_25: float | None
    cota_26: float | None
    cota_27: float | None
    cota_28: float | None
    cota_29: float | None
    cota_30: float | None
    cota_31: float | None
    cota_01_status: bool | None
    cota_02_status: bool | None
    cota_03_status: bool | None
    cota_04_status: bool | None
    cota_05_status: bool | None
    cota_06_status: bool | None
    cota_07_status: bool | None
    cota_08_status: bool | None
    cota_09_status: bool | None
    cota_10_status: bool | None
    cota_11_status: bool | None
    cota_12_status: bool | None
    cota_13_status: bool | None
    cota_14_status: bool | None
    cota_15_status: bool | None
    cota_16_status: bool | None
    cota_17_status: bool | None
    cota_18_status: bool | None
    cota_19_status: bool | None
    cota_20_status: bool | None
    cota_21_status: bool | None
    cota_22_status: bool | None
    cota_23_status: bool | None
    cota_24_status: bool | None
    cota_25_status: bool | None
    cota_26_status: bool | None
    cota_27_status: bool | None
    cota_28_status: bool | None
    cota_29_status: bool | None
    cota_30_status: bool | None
    cota_31_status: bool | None

    model_config = ConfigDict(
        populate_by_name=True, alias_generator=lambda s: s.title()
    )


class DadosDoMesVazao(_DadoDiario):
    vazao_01: float | None
    vazao_02: float | None
    vazao_03: float | None
    vazao_04: float | None
    vazao_05: float | None
    vazao_06: float | None
    vazao_07: float | None
    vazao_08: float | None
    vazao_09: float | None
    vazao_10: float | None
    vazao_11: float | None
    vazao_12: float | None
    vazao_13: float | None
    vazao_14: float | None
    vazao_15: float | None
    vazao_16: float | None
    vazao_17: float | None
    vazao_18: float | None
    vazao_19: float | None
    vazao_20: float | None
    vazao_21: float | None
    vazao_22: float | None
    vazao_23: float | None
    vazao_24: float | None
    vazao_25: float | None
    vazao_26: float | None
    vazao_27: float | None
    vazao_28: float | None
    vazao_29: float | None
    vazao_30: float | None
    vazao_31: float | None
    vazao_01_status: bool | None
    vazao_02_status: bool | None
    vazao_03_status: bool | None
    vazao_04_status: bool | None
    vazao_05_status: bool | None
    vazao_06_status: bool | None
    vazao_07_status: bool | None
    vazao_08_status: bool | None
    vazao_09_status: bool | None
    vazao_10_status: bool | None
    vazao_11_status: bool | None
    vazao_12_status: bool | None
    vazao_13_status: bool | None
    vazao_14_status: bool | None
    vazao_15_status: bool | None
    vazao_16_status: bool | None
    vazao_17_status: bool | None
    vazao_18_status: bool | None
    vazao_19_status: bool | None
    vazao_20_status: bool | None
    vazao_21_status: bool | None
    vazao_22_status: bool | None
    vazao_23_status: bool | None
    vazao_24_status: bool | None
    vazao_25_status: bool | None
    vazao_26_status: bool | None
    vazao_27_status: bool | None
    vazao_28_status: bool | None
    vazao_29_status: bool | None
    vazao_30_status: bool | None
    vazao_31_status: bool | None

    model_config = ConfigDict(
        populate_by_name=True, alias_generator=lambda s: s.title()
    )


class _DadoTelemetrica(BaseModel, ABC):
    codigoestacao: int = Field(alias="codigoestacao")
    chuva_adotada: float | None
    chuva_adotada_status: bool | None
    cota_adotada: float | None
    cota_adotada_status: bool | None
    data_atualizacao: datetime | None
    data_hora_medicao: datetime
    vazao_adotada: float | None
    vazao_adotada_status: bool | None

    model_config = ConfigDict(alias_generator=lambda s: s.title())


class DadoTelemetricaAdotada(_DadoTelemetrica):
    model_config = ConfigDict(alias_generator=lambda s: s.title())


class DadoTelemetricaDetalhada(_DadoTelemetrica):
    bateria: float | None
    chuva_acumulada: float | None
    chuva_acumulada_status: float | None
    cota_display: float | None
    cota_display_status: bool | None
    cota_manual: float | None
    cota_manual_status: bool | None
    cota_sensor: float | None
    cota_sensor_status: bool | None
    pressao_atmosferica: float | None
    pressao_atmosferica_status: bool | None
    temperatura_agua: float | None
    temperatura_agua_status: bool | None
    temperatura_interna: float | None

    model_config = ConfigDict(alias_generator=lambda s: s.title())


class DadoDiarioVazaoOriginalDaAPI(BaseModel):
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


class DadoTelemetricaAdotadaOriginalDaAPI(BaseModel):
    codigoestacao: int
    Chuva_Adotada: float | None
    Chuva_Adotada_Status: bool | None
    Cota_Adotada: float | None
    Cota_Adotada_Status: bool | None
    Data_Atualizacao: datetime
    Data_Hora_Medicao: datetime
    Vazao_Adotada: float | None
    Vazao_Adotada_Status: bool | None


class DadoTelemetricaDetalhadaOriginalDaAPI(BaseModel):
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
